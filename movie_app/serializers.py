from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


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


class DirectorCreateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=10, max_length=100)


class MovieCreateSelializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=20)
    description = serializers.CharField(min_length=20, max_length=1000)
    duration = serializers.CharField(min_length=30, max_length=240)
    director = serializers.IntegerField(min_value=1)


class ReviewCreateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1, max_length=1000)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    movie = serializers.IntegerField(min_value=1)

    def validate_director(self, director): # 9
        try:
            Director.objects.get(id=director)
        except Director.DoesNotExist:
            raise ValidationError('Director Not Found')
        return director

    def validate_movie(self, movie): # 9
        try:
            Movie.objects.get(id=movie)
        except Movie.DoesNotExist:
            raise ValidationError('Movie Not Fount')
        return movie

    def validate_title(self, title):
        if Movie.objects.filter(title=title):
            raise ValidationError('title must be unique')
        return title
