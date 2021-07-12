from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Movie, Director, Actor, Genre, Screenshot
from .serializers import (
    MovieSerializer, 
    DirectorSerializer, 
    ActorSerializer, 
    GenreSerializer, 
    ScreenshotSerializer
)

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.order_by('id')
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class DirectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Director.objects.order_by('id')
    serializer_class = DirectorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ActorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.order_by('id')
    serializer_class = ActorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.order_by('id')
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']