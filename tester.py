import os
import requests

# import csv

from dotenv import load_dotenv

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

movie_name = "In The Mood For Love"
details = []
url = f"https://www.omdbapi.com/?t={movie_name}&plot=full&apikey={OMDB_API_KEY}&"
response = requests.get(url)
json_response = response.json()


attribute_to_remove_list = [
    "Rated",
    "Writer",
    "Language",
    "Country",
    "Awards",
    "Metascore",
    "imdbID",
    "DVD",
    "BoxOffice",
    "Production",
    "Website",
]
attributes = [key for key in json_response]

for i in range(len(json_response)):
    if attributes[i] in attribute_to_remove_list:
        json_response.pop(attributes[i])
        # print(f"Popped {attributes[i]}")

for key, value in json_response.items():
    print(key, " -> ", value)
