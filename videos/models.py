from core.models import PublishStateOptions
from django.db import models
from django.utils import timezone


class VideoQuerySet(models.QuerySet):
    '''
    VideoQuerySet is a custom queryset for Video model.

    It is used to filter out videos that are published.
    '''

    def published(self):
        return self.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte=timezone.now()
        )


class VideoManager(models.Manager):
    '''
    VideoManager is a custom manager for Video model.

    It is used to filter out videos that are published.
    '''

    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Video(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        help_text='A "slug" is a unique URL-friendly title for video. e.g. "my-cat-is-cute"',
        max_length=100,
        unique=True,
        blank=True, null=True
    )
    description = models.TextField()
    video_id = models.CharField(max_length=220, unique=True)
    size = models.CharField(
        help_text='The size of the video in bytes (e.g. "123456789"). or "N/A" if the video is unavailable.',
        max_length=100,
        blank=True, null=True

    )
    state = models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)

    number_of_views = models.IntegerField()
    number_of_likes = models.IntegerField()
    number_of_dislikes = models.IntegerField()
    number_of_comments = models.IntegerField()
    number_of_shares = models.IntegerField()
    number_of_downloads = models.IntegerField()
    number_of_reports = models.IntegerField()
    number_of_ratings = models.IntegerField()
    number_of_favorites = models.IntegerField()

    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    objects = VideoManager()

    class Meta:
        ordering = ['-timestamp', '-updated']

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        'auth.User',
        related_name='comments',
        on_delete=models.CASCADE
    )
    # Note: Just for testing purposes we are using default user.
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField()
