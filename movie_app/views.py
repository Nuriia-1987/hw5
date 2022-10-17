from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from .models import Director, Movie, Review
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView, ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorListSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class DirectorItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorListSerializer
    lookup_field = 'id'


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class MovieItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    lookup_field = 'id'


class ReviewListAPIVies(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class ReviewItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    lookup_field = 'id'


class MoviesReviewsListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer2
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


# @api_view(['GET', 'POST'])
# def director_view(request):
#     if request.method == 'GET':
#         director = Director.objects.all()
#         data = DirectorListSerializer(director, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = DirectorCreateSerializer(data=request.dsta)
#         if not serializer.is_valid():
#             return Response(data={'message': 'data with errors',
#                                   'errors': serializer.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         director = Director.objects.create(
#             name=request.data.get('name')
#         )
#         director.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data={'message': 'Successfully created!'})
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def director_item_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'Director not fount'})
#     if request.method == 'GET':
#         serializer = DirectorListSerializer(director)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(data={'message': 'Successfully removed'},
#                         status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = DirectorCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         director.name = request.data.get('name')
#         return Response(data={'message': 'Successfully updated',
#                               'director': DirectorListSerializer(director).data})


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def movie_view(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         data = MovieListSerializer(movie, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = MovieCreateSelializer(data=request.dsta)
#         if not serializer.is_valid():
#             return Response(data={'message': 'data with errors',
#                                   'errors': serializer.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         movies = Movie.objects.create(
#             title=request.data.get('title'),
#             description=request.data.get('description'),
#             duration=request.data.get('duration'),
#             director_id=request.data.get('director')
#         )
#         movies.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data={'message': 'Successfully created!'})
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_item_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'Movie not found'})
#     if request.method == 'GET':
#         serializer = MovieListSerializer(movie)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(data={'message': 'Successfully removed'},
#                         status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = MovieCreateSelializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie.title = request.data.get('title')
#         movie.description = request.data.get('description')
#         movie.duration = request.data.get('duration')
#         movie.director_id = request.data.get('director')
#         movie.save()
#         return Response(data={'message': 'Successfully updated',
#                               'movie': MovieListSerializer(movie).data})


# @api_view(['GET', 'POST'])
# def review_view(request):
#     if request.method == 'GET':
#         review = Review.objects.all()
#         data = ReviewListSerializer(review, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = ReviewCreateSerializer(data=request.dsta)
#         if not serializer.is_valid():
#             return Response(data={'message': 'data with errors',
#                                   'errors': serializer.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         review = Review.objects.create(
#             text=request.data.get('text'),
#             stars=request.method.get('stars'),
#             movie_id=request.method.get('movie')
#         )
#         review.save()
#         return Response(status=status.HTTP_201_CREATED,
#                         data={'message': 'Successfully created!'})
#
#
# @api_view(['GET', 'PUT', "DELETE"])
# def review_item_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'Review not fount'})
#     if request.method == 'GET':
#         serializer = ReviewListSerializer(review)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(data={'message': 'Successfully removed'},
#                         status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = ReviewCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review.text = request.data.get('text'),
#         review.stars = request.data.get('stars'),
#         review.movie_id = request.data.get('movie')
#         return Response(data={'message': 'Successfully updated',
#                         'review': ReviewListSerializer(review).data})


# @api_view(['GET'])
# def movies_review_view(request):
#     review = Review.objects.all()
#     data = ReviewListSerializer2(review, many=True).data
#     return Response(data=data)
