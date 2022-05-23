from rest_framework import generics, permissions

from movies.models.genre_model import Genre
from movies.serializers.genre_serializer import GenreSerializer


class GenreListView(generics.ListAPIView):
    ''' List all genres. '''
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.AllowAny,)
