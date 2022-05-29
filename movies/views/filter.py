from django_filters import rest_framework as filters

from movies.models.movies_model import Movie


class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    year = filters.NumberFilter(field_name='year', lookup_expr='exact')
    genres = filters.CharFilter(field_name='genre', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['title', 'year', 'genres']
