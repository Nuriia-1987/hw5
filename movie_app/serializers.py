from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name '.split()


class MovieListSerializer(serializers.ModelSerializer):
    director = DirectorListSerializer()

    class Meta:
        model = Movie
        fields = 'id title description duration reviews director director_name rating'.split()


class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()

    class Meta:
        model = Review
        fields = 'id text movie stars'.split()


class MovieListSerializer2(serializers.ModelSerializer):
    director = DirectorListSerializer()

    class Meta:
        model = Movie
        fields = 'id title director rating'.split()


class ReviewListSerializer2(serializers.ModelSerializer):
    movie = MovieListSerializer2()

    class Meta:
        model = Review
        fields = 'id movie text '.split()
