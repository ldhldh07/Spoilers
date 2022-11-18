from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    is_staff = models.BooleanField(null=True)
    wish_list = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE)
