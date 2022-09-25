from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorListSerializer, MovieListSerializer, ReviewListSerializer
from .models import Director, Movie, Review


@api_view(['GET'])
def director_view(request):
    director = Director.objects.all()
    data = DirectorListSerializer(director, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_view(request):
    movie = Movie.objects.all()
    data = MovieListSerializer(movie, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_view(request):
    review = Review.objects.all()
    data = ReviewListSerializer(review, many=True).data
    return Response(data=data)
