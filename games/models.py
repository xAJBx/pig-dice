from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    release_year = models.IntegerField()
    picture_url = models.CharField(max_length=2040)
    date_created = models.DateTimeField(default=timezone.now)
    age_range = models.CharField(max_length=255)
    number_players = models.CharField(max_length=255)
    time_of_play = models.CharField(max_length=255)
    board_game_atlas_id = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

#build atlas table store api data?
