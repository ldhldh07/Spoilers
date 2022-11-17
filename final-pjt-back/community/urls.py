from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_pk>/comments/',views.create_comment),
]
