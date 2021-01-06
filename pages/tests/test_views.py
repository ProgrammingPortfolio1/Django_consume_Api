
from django.test import TestCase, Client
from django.urls import reverse
import json
from pages.views import index, info, posts, photos

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.info_url = reverse('info', args=['1'])
        self.posts_url = reverse('posts', args=['1'])
        self.photos_url = reverse('photos', args=['1'])

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_info_GET(self):
        response = self.client.get(self.info_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'info.html')

    def test_posts_GET(self):
        response = self.client.get(self.posts_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')

    def test_photos_GET(self):
        response = self.client.get(self.photos_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos.html')

