from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorListSerializer, MovieListSerializer, ReviewListSerializer, ReviewListSerializer2
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def director_view(request):
    director = Director.objects.all()
    data = DirectorListSerializer(director, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not fount'})
    serializer = DirectorListSerializer(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_view(request):
    movie = Movie.objects.all()
    data = MovieListSerializer(movie, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found'})
    serializer = MovieListSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_view(request):
    review = Review.objects.all()
    data = ReviewListSerializer(review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not fount'})
    serializer = ReviewListSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_review_view(request):
    review = Review.objects.all()
    data = ReviewListSerializer2(review, many=True).data
    return Response(data=data)
