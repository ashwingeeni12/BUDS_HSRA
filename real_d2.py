# new changes to real_d.py

import googlemaps
from datetime import datetime
import re
import html
from geopy.distance import geodesic
import time
from speech_text import *
from text_speech import *
from gps import *
import threading
import RPi.GPIO as GPIO

# Function to calculate distance between current location and next turn
def calculate_distance(current_loc, next_turn):
    return geodesic(current_loc, next_turn).feet

# Function to get real-time user location (mock implementation)
def get_current_location():
    coords = location()
    latitude = coords[0]
    longitude = coords[1]
    return (latitude, longitude)

def navigation_process():
    site = ""
    sites = stt()  # Get start and end locations using speech-to-text

    apiKey = "AIzaSyBP0A4jy_5ydtdGR0qtQ14glSJkF4Jw9IM"
    map_client = googlemaps.Client(apiKey)

    # Takes start and end locations from user
    start = sites[0]
    end = sites[1]
    print(str(start))
    print(str(end))
    mode = "walking"
    # This requests the directions
    directions = map_client.directions(start, end, mode=mode)

    # Loop through the directions and provide instructions
    x = 0
    for route in directions:
        for leg in route['legs']:
            for step in leg['steps']:
                # Cleans up instructions to print
                clean_instructions = re.sub('<[^<]+?>', '', html.unescape(step['html_instructions']))
                tts(clean_instructions)
                next_turn_location = (step['end_location']['lat'], step['end_location']['lng'])

                instruction_given = False
                while not instruction_given:
                    current_location = get_current_location()

                    distance = calculate_distance(current_location, next_turn_location)

                    if 40 <= distance <= 42:
                        tts(clean_instructions + " in 40 feet")
                    elif 10 <= distance <= 12:
                        tts(clean_instructions + " in 10 feet")
                    elif distance <= 2:
                        tts(clean_instructions + " in 2 feet")
                        instruction_given = True
                    x += 1

def switch_monitor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        input_state = GPIO.input(18)  # Read the state of the switch
        if input_state == GPIO.LOW:  # If switch is turned on (assuming active low)
            print("Switch turned on, starting navigation process.")
            navigation_thread = threading.Thread(target=navigation_process)
            navigation_thread.start()
            navigation_thread.join()  # Wait for the navigation process to complete
        time.sleep(0.1)

if __name__ == "__main__":
    switch_monitor()
