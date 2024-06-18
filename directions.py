import googlemaps
from datetime import datetime
import re
import html

apiKey = "AIzaSyBP0A4jy_5ydtdGR0qtQ14glSJkF4Jw9IM"

# Use API key here
map_client = googlemaps.Client(apiKey)

#Takes start and end locations from user
start = input("Enter your start location: ")
end = input("Enter your end location: ")

#walking or driving directions
mode = input("Enter your mode of transportation: ")

#This requests the directions
directions = map_client.directions(start, end, mode= mode)

url = "https://maps.googleapis.com/maps/api/directions/json?origin=New+York+City&destination=Washington,+DC&key=AIzaSyBP"


# Prints out the directions
for route in directions:
 for leg in route['legs']:
   for step in leg['steps']:
      #print(step['html_instructions'])
     
     clean_instructions = re.sub('<[^<]+?>', '', html.unescape(step['html_instructions']))
     print(clean_instructions)
      

