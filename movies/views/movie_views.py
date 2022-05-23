from datetime import datetime

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from core.models import MovieStatusOptions
from movies.models.movies_model import Movie
from movies.serializers.movie_serializer import MovieSerializer
from utils.response import quick_error_response, quick_success_response


class MovieListView(generics.ListAPIView):
    ''' List all RELEASED movies. '''
    queryset = Movie.objects.filter(status=MovieStatusOptions.RELEASED)
    serializer_class = MovieSerializer
    permission_classes = (permissions.AllowAny,)


class MovieDetailView(generics.RetrieveAPIView):
    ''' Retrieve a movie by id. '''
    queryset = Movie.objects.filter(status=MovieStatusOptions.RELEASED)
    serializer_class = MovieSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            movie.recently_viewed = datetime.now()
            movie.recently_watched = True
            movie.save()
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return quick_error_response(status.HTTP_404_NOT_FOUND, 'Movie not found.')
