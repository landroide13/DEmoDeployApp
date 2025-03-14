from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Index

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def average_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:     
            return sum / len(ratings)
        else:
            return 0    

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __int__(self):
        return self.stars

    class Meta:
        unique_together = (('user', 'movie'),)
        # index_together = (('user', 'movie'),)
        indexes = [
            Index(fields=['user', 'movie']),
        ]