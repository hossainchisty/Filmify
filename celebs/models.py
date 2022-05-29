from django.db import models


class Celebrity(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='cloud/photo/celebs')
    biography = models.TextField()
    age = models.IntegerField()
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(
        verbose_name='Gender',
        max_length=7,
        choices=GENDER,
    )
    place_of_birth = models.CharField(
        verbose_name='Place of Birth',
        max_length=100
    )
    birthday_date = models.DateField(
        verbose_name='Birthday'
    )
    died_date = models.DateField(null=True, blank=True)

    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    tiktok = models.URLField(null=True, blank=True)
    snapchat = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    known_for = models.ManyToManyField('movies.Movie', related_name='known_for')
    movies = models.ManyToManyField('movies.Movie', related_name='movies')
    recently_viewed = models.DateTimeField(auto_now_add=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        ''' String for representing the Model'''
        return self.name
