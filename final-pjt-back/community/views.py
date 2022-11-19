from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status

from .models import Comment
from movies.models import Movie
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated



# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serialzer = CommentSerializer(data=request.data)
    user_pk = request.data.get('user_id')
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if serialzer.is_valid(raise_exception=True):
        serialzer.save(movie=movie, user=user)
        return Response(serialzer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # elif request.method == 'PUT':
    #     serializer = CommentSerializer(comment, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)
