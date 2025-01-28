import os    
import csv
import requests
import json

from dotenv import load_dotenv

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

movie_name = "At Eternity's Gate"
details = []
url = f"https://www.omdbapi.com/?t={movie_name}&plot=full&apikey={OMDB_API_KEY}&"
response = requests.get(url)
response.json
obj = json.loads(response.text)
# output = json.dumps(obj, indent=4)
# print(output)
# print(type(output))
t = json.dumps(obj, indent = 4)
output = json.loads(t)
# print(output)
for i in output:
    print(i)
# for data in output:
#     t = output[1]
#     print(t)
    # details.append(t)

# print("Printing details")
# print(details)

# def extract_movie_name_from_csv():
#     movie_name = ""
#     with open('Movies.csv', newline='') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#         for row in reader:
#             movie_name = row[0]
#             url = f"https://www.omdbapi.com/?t={movie_name}&plot=full&apikey={OMDB_API_KEY}&"
#             response = requests.get(url)
#             response.json
#             obj = json.loads(response.text)
#             print(json.dumps(obj, indent=4))
#             print("\n-----------------------\n")


#     return movie_name


# extract_movie_name_from_csv()
