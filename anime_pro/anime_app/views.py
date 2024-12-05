from django.shortcuts import render
from .models import NewUser,UserPreferences
from .serializers import RegistrationSerializer, LoginSerializer,UserPreferencesSerializer,AnimeSearchSerializer,AnimeRecommendationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
import requests

def get_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

class RegistrationApiView(APIView):
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"MSG":"User regisration complete."},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginApiView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_token(user)
                return Response({"token":token,"msg":"login successfull"},status=status.HTTP_200_OK)
            return Response({"msg":"email and password doesn't match"},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

ANILIST_API_URL = "https://graphql.anilist.co"

class AnimeSearchView(APIView):
    def get(self, request):
        serializer = AnimeSearchSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        query = """
        query ($search: String, $genre: String) {
            Page {
                media(search: $search, genre: $genre, type: ANIME) {
                    id
                    title {
                        romaji
                    }
                    description
                    genres
                }
            }
        }
        """
        variables = {
            "search": serializer.validated_data.get('name'),
            "genre": serializer.validated_data.get('genre'),
        }
        response = requests.post(
            ANILIST_API_URL, json={"query": query, "variables": variables}
        )
        data = response.json()
        return Response(data['data']['Page']['media'], status=status.HTTP_200_OK)


class UserPreferencesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        preferences, created = UserPreferences.objects.get_or_create(user=request.user)
        serializer = UserPreferencesSerializer(preferences)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        preferences, created = UserPreferences.objects.get_or_create(user=request.user)
        serializer = UserPreferencesSerializer(preferences, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnimeRecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        preferences = UserPreferences.objects.filter(user=request.user).first()
        if not preferences:
            return Response({"error": "User preferences not set"}, status=status.HTTP_400_BAD_REQUEST)

        genres = preferences.favorite_genres.split(",")
        query = """
        query ($genres: [String]) {
            Page {
                media(genre_in: $genres, type: ANIME) {
                    id
                    title {
                        romaji
                    }
                    description
                    genres
                }
            }
        }
        """
        variables = {
            "genres": genres,
        }
        response = requests.post(
            ANILIST_API_URL, json={"query": query, "variables": variables}
        )
        data = response.json()
        return Response(data['data']['Page']['media'], status=status.HTTP_200_OK)