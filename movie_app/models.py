from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=10)
    director = models.ForeignKey(Director, max_length=100, on_delete=models.CASCADE,
                                 null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, max_length=100, on_delete=models.CASCADE,
                              null=True)

    def __str__(self):
        return self.text
