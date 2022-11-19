from rest_framework import serializers
from .models import Comment
from accounts.serializers import UserCommentSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserCommentSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'title', 'content', 'created_at', 'user')
        read_only_fields = ('movie',)
