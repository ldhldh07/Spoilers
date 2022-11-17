from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Comment
from movies.models import Movie
from .serializers import CommentSerializer


# Create your views here.
@api_view(['POST'])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serialzer = CommentSerializer(data=request.data)
    if serialzer.is_valid(raise_exception=True):
        # serialzer.save(movie=movie, user=request.user)
        serialzer.save(movie=movie)
        return Response(serialzer.data, status=status.HTTP_201_CREATED)
