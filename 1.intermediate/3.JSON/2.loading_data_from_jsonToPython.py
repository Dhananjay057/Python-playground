"""
json.loads(jsonstring) - process json string to Python type
json.load(filepointer) - loads json from a file and returns as a result 
                         of method python type
"""

import json

film = {
    "title" : "But I won't do it!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors" : ("Arkadiusz Wlodarczyk", "Wiolletta Wlodarczyk"),
    "budget" : None,
    "credits" : {
        "director" : "Arkadiusz Wlodarczyk",
        "writer" : "Alan Burger",
        "animator" : "Anime Animatrix"
    }
}

encodedRetrievedMovie = '{"title": "But I won\'t do it!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Wlodarczyk", "Wiolletta Wlodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Wlodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'
print(type(encodedRetrievedMovie))  # <class 'str'>
encodedMovie = json.loads(encodedRetrievedMovie)
print(encodedMovie)
print(type(encodedMovie)) # <class 'dict'>

with open("movies.json","r", encoding="utf-8") as file:
    result = json.load(file)

print(result)
print(type(result))
