import os    
import csv
import requests
import json

from dotenv import load_dotenv

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")


def extract_movie_name_from_csv():
    movie_name = ""
    with open('Movies.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        # print("here")
        for row in reader:
            movie_name = row[0]
            url = url=f"https://www.omdbapi.com/?t={movie_name}&plot=full&apikey={OMDB_API_KEY}&"
            response = requests.get(url)
            response.json
            obj = json.loads(response.text)
            print(json.dumps(obj, indent=4))
            print("\n-----------------------\n")
            # print(obj["Plot"])

    return movie_name


extract_movie_name_from_csv()
