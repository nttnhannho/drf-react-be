from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Category


class PostTestCases(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='django')
        User.objects.create_user(
            username='user1',
            password='123456',
        )

    def test_view_posts(self):
        url = reverse('blog_api:post-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        data = {
            'title': 'new',
            'author': 1,
            'excerpt': 'new',
            'content': 'new',
        }
        url = reverse('blog_api:post-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
