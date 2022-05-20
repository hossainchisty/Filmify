
from core.models import TimestampedModel
from django.db import models


class Genre(TimestampedModel):
    name = models.CharField(
        db_index=True,
        max_length=50
    )

    def __str__(self):
        return self.name
