from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorListSerializer, MovieListSerializer, ReviewListSerializer, ReviewListSerializer2
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        data = DirectorListSerializer(director, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        director = Director.objects.create(
            name=request.data.get('name')
        )
        director.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Successfully created!'})


@api_view(['GET', 'PUT', 'DELETE'])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not fount'})
    if request.method == 'GET':
        serializer = DirectorListSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(data={'message': 'Successfully removed'},
                        status=status.HTTP_204_NO_CONTENT)
    else:
        director.name = request.data.get('name')
        return Response(data={'message': 'Successfully updated',
                              'director': DirectorListSerializer(director).data})


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        data = MovieListSerializer(movie, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        movies = Movie.objects.create(
            title=request.data.get('title'),
            description=request.data.get('description'),
            duration=request.data.get('duration'),
            director_id=request.data.get('director')
        )
        movies.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Successfully created!'})

@api_view(['GET', 'PUT', 'DELETE'])
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Movie not found'})
    if request.method == 'GET':
        serializer = MovieListSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Successfully removed'},
                        status=status.HTTP_204_NO_CONTENT)
    else:
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director')
        movie.save()
        return Response(data={'message': 'Successfully updated',
                              'movie': MovieListSerializer(movie).data})


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewListSerializer(review, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        review = Review.objects.create(
            text=request.data.get('text'),
            stars=request.method.get('stars'),
            movie_id=request.method.get('movie')
        )
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Successfully created!'})


@api_view(['GET', 'PUT', "DELETE"])
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not fount'})
    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(data={'message': 'Successfully removed'},
                        status=status.HTTP_204_NO_CONTENT)
    else:
        review.text = request.data.get('text'),
        review.movie_id = request.data.get('movie')
        return Response(data={'message': 'Successfully updated',
                        'review': ReviewListSerializer(review).data})


@api_view(['GET'])
def movies_review_view(request):
    review = Review.objects.all()
    data = ReviewListSerializer2(review, many=True).data
    return Response(data=data)
