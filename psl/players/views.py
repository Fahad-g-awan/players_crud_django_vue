from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .apis.account import *
from .apis.player import *


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# @permission_classes([IsAuthenticated])
def players(request):
    """
    API view to handle players requests 
    """
    
    if request.method == "POST":
        return create_player(request.data)
    elif request.method == "GET":
        return get_players()
    elif request.method in ["PUT", "PATCH"]:
        return update_player(request.data)
    elif request.method == "DELETE":
        return delete_player(request.data)
    else:
        return Response({"error": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
 

@api_view(['POST'])
def auth(request):
    """
    API view to handle user authentication 
    """

    if request.method == "POST" and request.path == "/api/register/":
        return register(request)
    elif request.method == "POST" and request.path == "/api/login/":
        return user_login(request)
    elif request.method == "POST" and request.path == "/api/logout/":
        return user_logout(request)
    elif request.method == "POST" and request.path == "/api/refresh_token/":
        return refresh_token(request)
    else:
        return Response({"error": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
 



