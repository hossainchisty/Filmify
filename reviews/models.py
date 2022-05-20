from core.models import TimestampedModel
from django.db import models


class Review(TimestampedModel):
    """ A review of a movie. """

    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE
    )
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Review by {self.user}'
