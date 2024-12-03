from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Joke
from .serializers import JokeSerializer


# Create your views here.
class JokeListView(APIView):
    def get(self, request):
        jokes = Joke.objects.all()
        serializer = JokeSerializer(jokes,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    