from django.contrib import admin
from tvshows.models import Tvshow


@admin.register(Tvshow)
class TVShowAdmin(admin.ModelAdmin):
    '''
    Admin for TVShow model.
    '''
    list_display = ('episode_name', 'episode', 'season')
    list_filter = ('episode_name', 'episode', 'season')
    search_fields = ('episode_name', 'episode', 'season')
