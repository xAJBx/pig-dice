import django_filters
from .models import *

class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Games
        fields = '__all__'
        exclude = ['language', 'picture_url', 'date_created']
