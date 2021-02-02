from django.db import models

# Create your models here.


class Movie(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.CharField(max_length=4)
    Type = models.CharField(max_length=10)
    imdbID = models.CharField(max_length=11)

    def is_object_exists(self):
        return bool(Movie.objects.filter(imdbID=self.imdbID))
