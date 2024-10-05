from rest_framework.response import Response
from collections import defaultdict
from rest_framework import status

from ..models import *
import json


def create_player(data):
    """
    Function to create player
    """
    
    try:
        players_data = data.get("players") 
        
        if not players_data or not isinstance(players_data, list):
            return Response({"error": "Invalid or missing 'players' field in request."}, status=status.HTTP_400_BAD_REQUEST)

        created_players = []

        for player in players_data:
            team_name = player.get("team_name")
            name = player.get("name")
            username = player.get("username")
            email = player.get("email")

            if not team_name or not name or not username or not email:
                return Response({"error": "Missing required fields in one or more player."}, status=status.HTTP_400_BAD_REQUEST)
            
            if Players.objects.filter(username=username).exists():
                return Response({"error": f"player already exist for username: {username}."}, status=status.HTTP_400_BAD_REQUEST)
            if Players.objects.filter(email=email).exists():
                return Response({"error": f"player already exist for email: {email}."}, status=status.HTTP_400_BAD_REQUEST)
            
            team, created = Teams.objects.get_or_create(name=team_name)

            player = Players.objects.create(
                team=team,
                name=name,
                username=username,
                email=email
            )
            print(f"New player {player.name}")
        
            created_players.append({
                "id": player.id,
                "team": player.team.name,
                "name": player.name,
                "username": player.username,
                "email": player.email,
            })

        return Response({"message": "Data added", "data": created_players}, status=201)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

def get_players():
    """
    Function to get all players
    """

    try:
        players = Players.objects.select_related('team').all()

        if not players: 
            return Response({"message": "No players found."}, status=404)
        
        grouped_data = defaultdict(list)

        print("players", players)

        for player in players:
            team_name = player.team.name
            player_data = {
                "id": player.id,
                "name": player.name,
                "username": player.username,
                "email": player.email,
                "created_at": player.created_at,
                "updated_at": player.updated_at,
            }
            grouped_data[team_name].append(player_data)

        response_data = dict(grouped_data)

        return Response(response_data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def update_player(data):
    """
    Function to update player
    """

    try:
        players_data = data.get("players") 
        
        if not players_data or not isinstance(players_data, list):
            return Response({"error": "Invalid or missing 'players' field in request."}, status=status.HTTP_400_BAD_REQUEST)
        
        updated_players = []

        for player in players_data:
            print("-----", player)
            player_id = player.get("id")
            username = player.get("username")
            email = player.get("email")

            if not player_id:
                return Response({"error": "Player ID is required."}, status=status.HTTP_400_BAD_REQUEST)

            if Players.objects.filter(username=username).exclude(id=player_id).exists():
                return Response({"error": f"player already exist for username: {username}."}, status=status.HTTP_400_BAD_REQUEST)
            if Players.objects.filter(email=email).exclude(email=email).exists():
                return Response({"error": f"player already exist for email: {email}."}, status=status.HTTP_400_BAD_REQUEST)

            query_set = Players.objects.get(id=player_id) 
            print("====", query_set)

            query_set.name = player.get("name", query_set.name)
            query_set.username = player.get("username", query_set.username)
            query_set.email = player.get("email", query_set.email)

            query_set.save()
            updated_players.append(query_set.id)
        
        response_data = {
            "message": "Players updated successfully",
            "updated_players": updated_players
        }
        return Response(response_data, status=status.HTTP_200_OK)

    except Players.DoesNotExist:
        return Response({"error": f"Player with ID {player_id} not found."}, status=status.HTTP_404_NOT_FOUND)
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def delete_player(data):
    """
    Function to delete a player
    """

    try:
        player_id = data.get("id")

        if not player_id:
            return Response({"error": "Player ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        player = Players.objects.get(id=player_id)
        player.delete()

        return Response({"data": "Player deleted successfully!"}, status=204)
        
    except Players.DoesNotExist:
        return Response({"error": "Player not found."}, status=404)
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON."}, status=400)
    


