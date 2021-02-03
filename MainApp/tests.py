from django.test import TestCase

# Create your tests here.
from MainApp.models import Movie


class TestMovieModel(TestCase):
    imbdID = "111"

    def setUp(self):
        Movie.objects.create(imdbID=self.imbdID)

    def test_is_object_exist_false(self):
        movie = Movie.objects.get(imdbID=self.imbdID)
        Movie.objects.get(imdbID=self.imbdID).delete()
        self.assertFalse(movie.is_object_exists())
