from typing import Union

from django.http import HttpResponseNotFound

from MainApp.models import Movie
from conf.settings import settings
import requests


def get_movie_info_by_title(title: str):
    api_key = settings.access_token
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={title}"
    response = requests.get(url).json()

    if "Search" in response:
        return [Movie(Title=item["Title"], Year=item["Year"], Type=item["Type"], imdbID=item["imdbID"]) for item in response["Search"]]

    return {}


def get_movie_info_by_id(movie_id: str) -> Union[Movie, HttpResponseNotFound]:
    api_key = settings.access_token
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={movie_id}"
    response = requests.get(url).json()

    return response

