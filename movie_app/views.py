from rest_framework import generics
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

# Список всех режиссеров
class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

# Подробная информация о режиссере
class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

# Список всех фильмов
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Подробная информация о фильме
class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Список всех отзывов
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Подробная информация об отзыве
class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
