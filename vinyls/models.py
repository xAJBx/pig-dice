from django.db import models
from django.utils import timezone


class Genres(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre


class Vinyls(models.Model):
    vinyl_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=255)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    artists = models.CharField(max_length=255)
    release_year = models.IntegerField()
    picture_url = models.CharField(max_length=2040)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


