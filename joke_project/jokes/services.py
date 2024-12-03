import requests
from .models import Joke

JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&amount=10"

def fetch_jokes():
    response = requests.get(JOKE_API_URL)
    jokes_data = response.json()
    return jokes_data['jokes']

def store_jokes(jokes):
    for joke in jokes:
        joke_obj = Joke(
            category=joke.get("category"),
            type=joke.get("type"),
            joke=joke.get("joke"),
            setup=joke.get("setup"),
            delivery=joke.get("delivery"),
            nsfw=joke["flags"].get("nsfw", False),
            political=joke["flags"].get("political", False),
            sexist=joke["flags"].get("sexist", False),
            safe=joke.get("safe", True),
            lang=joke.get("lang", "en"),
        )
        joke_obj.save()
    

def fetch_and_store_jokes():
    jokes = fetch_jokes()
    store_jokes(jokes)