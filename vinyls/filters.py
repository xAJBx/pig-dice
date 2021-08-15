import django_filters
from .models import *

class VinylFilter(django_filters.FilterSet):
    class Meta:
        model = Vinyls
        fields = '__all__'
        exclude = ['language', 'picture_url', 'date_created']

