from django.shortcuts import render
from .serializers import UserReigistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


# Create your views here.
# @api_view(['POST'])
# def signup(request):
#     if request.user.is_authenticated:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     password = request.data.get('password')
#     password2 = request.data.get('password2')
#     if password != password2:
#         error_message = {
#             'message' : '비밀번호 불일치'
#         }
#         return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

#     serializer = UserReigistrationSerializer(data=request.data)
    
#     if serializer.is_valid(raise_exception=True):
#         user = serializer.save()
#         token = Token.objects.create(user=user)
#         user.set_password(password)
#         data = {
#             'Token': token.key
#             }
            
#         return Response(data, status=status.HTTP_201_CREATED)

