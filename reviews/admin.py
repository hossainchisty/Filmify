from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    '''
    Admin for Review model.
    '''
    list_display = ('user', 'content')
