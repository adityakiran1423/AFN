import os
import csv
import requests

# import json

from dotenv import load_dotenv

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

def extract_movie_name_from_csv():
    movie_name = ""
    with open("Movies.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in reader:
            movie_name = row[0]
            url = f"https://www.omdbapi.com/?t={movie_name}&plot=full&apikey={OMDB_API_KEY}&"
            response = requests.get(url)
            # json_response = response.json()
            pruned_ouput = prune_api_response(response.json())

    return pruned_ouput


def prune_api_response(response):
    if response['Response'] == 'False':
        # think of something better to return 
        return "movie not found"
    
    attribute_to_remove_list = [
        'Rated',
        'Writer',
        'Language',
        'Country',
        'Awards',
        'Metascore',
        'imdbID',
        'DVD',
        'BoxOffice',
        'Production',
        'Website',
    ]

    # print(response)
    attributes = [key for key in response]

    for i in range(len(response)):
        if attributes[i] in attribute_to_remove_list:
            response.pop(attributes[i])

    for key, value in response.items():
        print(key, " -> ", value)

    return response


extract_movie_name_from_csv()
