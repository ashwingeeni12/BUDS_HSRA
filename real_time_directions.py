import googlemaps
from datetime import datetime
import re
import html
from geopy.distance import geodesic
import speech_text
from text_speech import *

import time

# Use API key here
apiKey = "AIzaSyBP0A4jy_5ydtdGR0qtQ14glSJkF4Jw9IM"
map_client = googlemaps.Client(apiKey)

# Takes start and end locations from user
start = speech_text.origin
end = speech_text.destination

# Walking or driving directions
mode = walking

# This requests the directions
directions = map_client.directions(start, end, mode=mode)

# Function to calculate distance between current location and next turn
def calculate_distance(current_loc, next_turn):
    return geodesic(current_loc, next_turn).meters


# Function to get real-time user location (mock implementation)
def get_current_location():
    latitude = float(input("Enter your current latitude: "))
    longitude = float(input("Enter your current longitude: "))
    return (latitude, longitude)

# Loop through the directions and provide instructions
for route in directions:
    for leg in route['legs']:
        for step in leg['steps']:
            clean_instructions = re.sub('<[^<]+?>', '', html.unescape(step['html_instructions']))
            tts(clean_instructions)
            while True:
                current_location = get_current_location()
                distance = calculate_distance(current_location, next_turn_location)
                if distance <= 42 and distance >= 40:  # If within 40 meters of the turn
                    tts(clean_instructions + " in 40 meters)
                if distance >= 10 and distance <= 12: 
                    tts(clean_instructions + " in 10 meters) 
                if distance <= 2: 
                    tts(clean_instructions + " in 2 meters)
                    break 

            
