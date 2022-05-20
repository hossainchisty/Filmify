from taggit.managers import TaggableManager

from awards_and_events.models import Award
from celebs.models import Celebrity
from core.models import MovieStatusOptions, TimestampedModel
from django.db import models
from reviews.models import Review
from videos.models import Video

from .genre_model import Genre


class Movie(TimestampedModel):
    title = models.CharField(db_index=True, max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    runtime = models.DurationField()
    genre = models.ManyToManyField(Genre)
    rating = models.IntegerField(blank=True, null=True)
    # Note: This is only for trailer videos. It is not a field for the movie itself.
    trailer = models.OneToOneField(
        Video,
        related_name='Trailer',
        on_delete=models.CASCADE,
        blank=True, null=True,
    )
    production = models.CharField(
        help_text='e.g. "Sony Pictures, Marvel Studios, Universal Studios", etc.',
        max_length=50,
        blank=True, null=True
    )
    image = models.ImageField(upload_to='movies')
    director = models.CharField(max_length=10)
    writer = models.CharField(max_length=10)
    cast = models.ForeignKey(
        Celebrity,
        on_delete=models.DO_NOTHING,
        null=True, blank=True,
    )
    awards = models.ManyToManyField(Award)
    status = models.CharField(
        max_length=2,
        default=MovieStatusOptions.DRAFT,
        choices=MovieStatusOptions.choices,
        help_text='Draft means not yet published. Published means it is live.'
    )
    language = models.CharField(
        verbose_name='Original Language',
        max_length=100
    )

    budget = models.DecimalField(
        verbose_name='Budget',
        max_digits=100, decimal_places=2
    )

    revenue = models.DecimalField(
        verbose_name='Revenue',
        max_digits=100, decimal_places=2
    )

    keywords = TaggableManager()

    popularity = models.IntegerField()
    is_trending = models.BooleanField(default=False)
    # TODO: is_featured = models.BooleanField(default=False)
    is_watched = models.BooleanField(default=False)

    recently_watched = models.BooleanField(default=False)
    recently_viewed = models.DateTimeField(auto_now_add=True)
    add_to_favorite = models.ManyToManyField('auth.User', blank=True)

    reviews = models.OneToOneField(
        Review,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
