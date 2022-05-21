from rest_framework import serializers

from movies.models.movies_model import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'year', 'runtime', 'genre', 'rating', 'trailer', 'production',
                  'image', 'director', 'writer', 'cast', 'awards', 'status', 'language', 'budget', 'revenue']
