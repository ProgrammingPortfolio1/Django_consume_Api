
from django.test import TestCase
from django.urls import reverse, resolve
from pages.views import index, info, posts, photos
import re

class YourTestClass(TestCase):

    def test_index(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_info(self):
        url = reverse('info', args=['1'])
        self.assertEquals(resolve(url).func, info)

    def test_posts(self):
        url = reverse('posts', args=['1'])
        self.assertEquals(resolve(url).func, posts)

    def test_photos(self):
        url = reverse('photos', args=['1'])
        self.assertEquals(resolve(url).func, photos)


