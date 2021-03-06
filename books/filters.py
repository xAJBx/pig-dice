import django_filters
from .models import *

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Books
        fields = '__all__'
        exclude = ['book_id', 'language', 'edition', 'picture_url', 'date_created', 'google_books_id']
