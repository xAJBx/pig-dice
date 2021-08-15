from django.db import models
from django.utils import timezone


class Category(models.Model):
    main = models.CharField(max_length=255)
    sub = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.main} {self.sub}'

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=2040)
    publication_date = models.IntegerField()
    edition = models.CharField(max_length=255)
    picture_url = models.CharField(max_length=2040)
    date_created = models.DateTimeField(default=timezone.now)
    google_books_id = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
