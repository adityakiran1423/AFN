import requests
import json

def main():
    movie_name="How To Make Millions Before Grandma Dies"
    movie_name.replace(" ", "+")
    print(movie_name)
    url=f"https://www.omdbapi.com/?t={movie_name}&plot=full&apikey=put_api_key_here&"
    response = requests.get(url)
    response.json()
    obj = json.loads(response.text)
    # json_formatted_str = json.dumps(obj, indent=4)
    print(json.dumps(obj, indent=4))
    print("\n-----------------------\n")
    print(obj["Plot"])

if __name__=="__main__":
    main()
