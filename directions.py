import googlemaps
from datetime import datetime
import re
import html
import speech_text

apiKey = "AIzaSyBP0A4jy_5ydtdGR0qtQ14glSJkF4Jw9IM"

# Use API key here
map_client = googlemaps.Client(apiKey)

#Takes start and end locations from user
start = speech_text.origin
end = speech_text.destination

#walking or driving directions
mode = input("Enter your mode of transportation: ")

#This requests the directions
directions = map_client.directions(start, end, mode= mode)


# Prints out the directions
for route in directions:
 for leg in route['legs']:
   for step in leg['steps']:
     #cleans up the output
     #removes html portions

     print("")
    
     clean_instructions = re.sub('<[^<]+?>', '', html.unescape(step['html_instructions']))
     print(clean_instructions)

     print("")

