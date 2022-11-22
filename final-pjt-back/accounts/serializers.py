from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie


class MovieWishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'movie_title', 'poster_path',)


class UserSerializer(serializers.ModelSerializer):
    wish_list = MovieWishListSerializer(many=True)

    class Meta:
        model = get_user_model()
        exclude=('password',)
        write_only_fields = ['password',]


class UserCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields=('id', 'username',)