from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'movie']
