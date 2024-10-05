from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status

from ..models import *
import json


def register(request):
    """
    Function to register user
    """

    try:
        data = json.loads(request.body)

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=400)

        user = User.objects.filter(username=username)

        if user.exists():
            return Response({"error": "User already exists."}, status=409)

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)

        user.save()

        return Response({"message": "User created."}, status=201)
        
    except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format"}, status=400)


def user_login(request):
    """
    Function to handle user login
    """

    try:
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=400)

        if not User.objects.filter(username=username).exists():
            return Response({"error": "Unauthorized: User not found"}, status=401)
        
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=401)
        else:
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            data = {
                "message": "Login successful",
                "access_token": access_token,
                "refresh_token": str(refresh)
            }
            return Response(data, status=status.HTTP_200_OK)
    
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON format"}, status=400)


def user_logout(request):
    """
    Function to handle user logout
    """

    try:
        token = request.data.get('refresh_token')

        if token is None:
            return Response({"error": "No refresh token provided"}, status=status.HTTP_400_BAD_REQUEST)

        refresh_token = RefreshToken(token)
        refresh_token.blacklist()

        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def refresh_token(request):
    """
    Function to refresh JWT access token using a refresh token.
    """

    try:
        data = request.data
        refresh_token = data.get("refresh_token")
        
        if not refresh_token:
            return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken(refresh_token)
        access_token = str(token.access_token)
        
        return Response({"access_token": access_token}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




