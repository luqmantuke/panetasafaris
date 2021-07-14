import django_filters
from .models import *

class TourFilter(django_filters.FilterSet):
    class Meta:
        model = Destination
        fields = {
            'name': ['icontains'],

        }