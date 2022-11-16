from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=50)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_title = models.TextField()
    date_opened = models.DateTimeField()
    overview = models.TextField()
    # trailer_key = models.TextField()
    review_searched = models.TextField()
    starring = models.ManyToManyField(Actor, related_name='filmography')
    genres_of_movie = models.ManyToManyField(Genre, related_name='movies_of_genre')



