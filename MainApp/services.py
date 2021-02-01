from MainApp.schemas import MovieInfo
from conf.settings import settings
import requests


def get_movie_info_by_title(title: str = None) -> MovieInfo:
    api_key = settings.access_token
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={title}"
    response = requests.get(url).json()

    if "Search" in response:
        return [MovieInfo.parse_obj(item) for item in response["Search"]]

    return {}


