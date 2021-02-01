from pydantic.main import BaseModel


class MovieInfo(BaseModel):
   Title: str
   Year: str
   Type: str
   imdbID: str
