from core.models import PublishStateOptions
from django.test import TestCase
from videos.models import Video


class VideoModelTestCase(TestCase):
    ''' Unit tests cases for the Video model '''

    def setUp(self):
        self.object = Video.objects.create(
            title='Test Video',
            slug='test-video',
            description='Test Description',
            video_id='123456789',
            size='1.6GB',
            state=PublishStateOptions.PUBLISH,
            number_of_views=14200,
            number_of_likes=2100,
            number_of_dislikes=1,
            number_of_comments=121,
            number_of_shares=1465,
            number_of_downloads=15346,
            number_of_reports=1,
            number_of_ratings=8,
            number_of_favorites=112,
            active=True
        )

    def test_title_field(self):
        ''' Test the title field '''
        title = self.object.title
        self.assertEqual(title, self.object.title)

    def test_valid_title(self):
        ''' Test the title field '''
        title = 'Test Video'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_valid_slug(self):
        ''' Test the slug field '''
        slug = 'test-video'
        qs = Video.objects.filter(slug=slug)
        self.assertTrue(qs.exists())

    def test_slug_field(self):
        ''' Test the slug field '''
        slug = self.object.slug
        self.assertEqual(slug, self.object.slug)

    def test_description_field(self):
        ''' Test the description field '''
        description = self.object.description
        self.assertEqual(description, self.object.description)

    def test_video_id_field(self):
        ''' Test the video_id field '''
        video_id = self.object.video_id
        self.assertEqual(video_id, self.object.video_id)

    def test_size_field(self):
        ''' Test the size field '''
        size = self.object.size
        self.assertEqual(size, self.object.size)

    def test_state_field(self):
        ''' Test the state field '''
        state = self.object.state
        self.assertEqual(state, self.object.state)

    def test_draft_state(self):
        ''' Test the draft state '''
        qs = Video.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertFalse(qs.exists())

    def test_published_state(self):
        ''' Test the published state '''
        published_qs = Video.objects.filter(
            state=PublishStateOptions.PUBLISH
        )
        self.assertTrue(published_qs.exists())

    def test_number_of_views_field(self):
        ''' Test the number_of_views field '''
        number_of_views = self.object.number_of_views
        self.assertEqual(number_of_views, self.object.number_of_views)

    def test_number_of_likes_field(self):
        ''' Test the number_of_likes field '''
        number_of_likes = self.object.number_of_likes
        self.assertEqual(number_of_likes, self.object.number_of_likes)

    def test_number_of_dislikes_field(self):
        ''' Test the number_of_dislikes field '''
        number_of_dislikes = self.object.number_of_dislikes
        self.assertEqual(number_of_dislikes, self.object.number_of_dislikes)

    def test_number_of_comments_field(self):
        ''' Test the number_of_comments field '''
        number_of_comments = self.object.number_of_comments
        self.assertEqual(number_of_comments, self.object.number_of_comments)

    def test_number_of_shares_field(self):
        ''' Test the number_of_shares field '''
        number_of_shares = self.object.number_of_shares
        self.assertEqual(number_of_shares, self.object.number_of_shares)

    def test_number_of_downloads_field(self):
        ''' Test the number_of_downloads field '''
        number_of_downloads = self.object.number_of_downloads
        self.assertEqual(number_of_downloads, self.object.number_of_downloads)

    def test_number_of_reports_field(self):
        ''' Test the number_of_reports field '''
        number_of_reports = self.object.number_of_reports
        self.assertEqual(number_of_reports, self.object.number_of_reports)

    def test_number_of_ratings_field(self):
        ''' Test the number_of_ratings field '''
        number_of_ratings = self.object.number_of_ratings
        self.assertEqual(number_of_ratings, self.object.number_of_ratings)

    def test_number_of_favorites_field(self):
        ''' Test the number_of_favorites field '''
        number_of_favorites = self.object.number_of_favorites
        self.assertEqual(number_of_favorites, self.object.number_of_favorites)

    def test_active_field(self):
        ''' Test the active field '''
        active = self.object.active
        self.assertEqual(active, self.object.active)

    def test_str_method(self):
        ''' Test the __str__ method '''
        self.assertEqual(str(self.object), self.object.title)
