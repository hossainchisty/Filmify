from django.db import models


class TimestampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``updated_at`` fields.
    """
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    #  A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        ordering = ['-created_at', '-updated_at']


class PublishStateOptions(models.TextChoices):
    # CONSTANT = DB_VALUE, USER_DISPLAY_VALUE
    PUBLISH = 'PU', 'Publish'
    DRAFT = 'DR', 'Draft'
    UNLISTED = 'UN', 'Unlisted'
    PRIVATE = 'PR', 'Private'
    REMOVED = 'RE', 'Removed'


class MovieStatusOptions(models.TextChoices):
    DRAFT = 'DR', 'Draft'
    PLANNED = 'PL', 'Planned'
    REMOVED = 'RE', 'Removed'
    RELEASED = 'RD', 'Released'
    CANCELLED = 'CA', 'Cancelled'
    INPRODUCTION = 'IP', 'In Production'
    POSTPRODUCTION = 'PP', 'Post Production'
