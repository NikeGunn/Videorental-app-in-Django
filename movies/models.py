from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083, default="")
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    date_created = models.DateTimeField(default = timezone.now)

    