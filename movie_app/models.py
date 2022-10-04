from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=20)
    director = models.ForeignKey(Director, max_length=100, on_delete=models.CASCADE,
                                 null=True)

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        try:
            return self.director.name
        except:
            return ''

    @property
    def rating(self):
        count = self.reviews.all().count()
        sum_ = sum(i.stars for i in self.reviews.all())
        try:
            return sum_ / count
        except ZeroDivisionError:
            return 0


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(default=5)
    movie = models.ForeignKey(Movie, max_length=100, on_delete=models.CASCADE,
                              null=True, related_name='reviews')

    def __str__(self):
        return self.text

