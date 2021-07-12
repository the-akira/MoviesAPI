from rest_framework import serializers
from .models import Movie, Director, Actor, Genre, Screenshot

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre 
        fields = ['id','name']

class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ['url']

class MovieSpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie 
        fields = ['id','title']

class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    cast = serializers.StringRelatedField(many=True)
    genre = serializers.StringRelatedField(many=True)
    screenshots = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie 
        fields = [
            'id',
            'title',
            'synopsis',
            'cover',
            'trailer',
            'screenshots',
            'director',
            'cast',
            'genre',
            'release_date',
            'running_time',
            'country',
            'language',
            'magnet',
            'created',
            'edited',
            'url'
        ]

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSpecificSerializer(many=True)

    class Meta:
        model = Actor 
        fields = ['id','name','photo','country','movies']

class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSpecificSerializer(many=True)

    class Meta:
        model = Director 
        fields = ['id','name','photo','country','movies']