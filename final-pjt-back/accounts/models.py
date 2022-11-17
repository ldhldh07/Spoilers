from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    is_staff = models.BooleanField()
    wish_list = models.ForeignKey(Movie, on_delete=models.CASCADE)