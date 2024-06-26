def d1(input):
    trig = "give me directions to "
    loc = input.lower().index(trig)
    input = input[loc + len(trig) : len(input)]
    return input
    
def d2(input):
    trig = "give me directions from "
    loc = input.lower().index(trig)
    input = input[loc + len(trig) : len(input)]
    input = input.split(" to ")
    return input

response = "Give me DIRECTIONS from UT Austin West Mall Station to 1800 Ur Mom"

origin = "" #raspberry pi location
destination = ""
if("give me directions to" in response.lower()):
    destination = d1(response)
else:
    o_words = d2(response)
    origin = o_words[0]
    destination = o_words[1]



