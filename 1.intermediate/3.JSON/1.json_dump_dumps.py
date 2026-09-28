"""
JSON

json.dumps(data) - saves data  from python --> JSON string
json.dump(data, nameOfFileHandler, ensure_ascii=False) -
                    saves data to nameOfFileHandler in JSON format

dump means drop, throw away, ditch
"""

import json

movie = {
    "title": "But I won't do it!",
    "release_year": 1969,
    "won_oscar": True,
    "actors": ("Arkadiusz Wlodarczyk", "Wiolletta Wlodarczyk"),
    "budget": None,
    "credits": {
        "director": "Arkadiusz Wlodarczyk",
        "writer": "Alan Burger",
        "animator": "Anime Animatrix"
    }
}

"""
{
    "title": "Ale ja nie będę tego robił!",
    "release_year": 1969,
    "won_oscar": true,
    "actors": [
        "Arkadiusz Wlodarczyk",
        "Wiolletta Wlodarczyk"
    ],
    "budget": null,
    "credits": {
        "director": "Arkadiusz Wlodarczyk",
        "writer": "Alan Burger",
        "animator": "Anime Animatrix"
    }
}
"""

encoded_movies = json.dumps(movie, ensure_ascii=False)
print(encoded_movies)

with open("movies.json","w", encoding="utf-8") as file:
    json.dump(movie, file, ensure_ascii=False)