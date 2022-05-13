from django.contrib import admin
from movies.models.genre_model import Genre
from movies.models.movies_model import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    ''' Admin for Movie model.'''
    list_display = ('title', 'year', 'director', 'rating')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ''' Admin for Genre model.'''
    list_display = ('name',)
