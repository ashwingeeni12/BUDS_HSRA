import googlemaps
from datetime import datetime
import re
import html
from geopy.distance import geodesic

import time

# Use API key here
apiKey = "AIzaSyBP0A4jy_5ydtdGR0qtQ14glSJkF4Jw9IM"
map_client = googlemaps.Client(apiKey)

# Takes start and end locations from user
start = input("Enter your start location: ")
end = input("Enter your end location: ")

# Walking or driving directions
mode = input("Enter your mode of transportation (driving, walking): ")

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
            next_turn_location = (step['end_location']['lat'], step['end_location']['lng'])
            print("\nNext instruction: ", clean_instructions)
            print("")

            while True:
                current_location = get_current_location()
                distance = calculate_distance(current_location, next_turn_location)
                print(f"Distance to next turn: {distance:.2f} meters")

                if distance < 50:  # If within 50 meters of the turn
                    print(f"Instruction: {clean_instructions}")
                    break

                time.sleep(10)  # Check location every 10 seconds
