from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import (
    Category,
    Post,
)


class CreatePostTestCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='django')
        User.objects.create_user(
            username='user1',
            password='123456',
        )
        Post.objects.create(
            category_id=1,
            title='post title',
            excerpt='post excerpt',
            content='post content',
            slug='post-title',
            author_id=1,
            status='published',
        )

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        category = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'

        self.assertEqual(author, 'user1')
        self.assertEqual(excerpt, 'post excerpt')
        self.assertEqual(title, 'post title')
        self.assertEqual(content, 'post content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'post title')
        self.assertEqual(str(category), 'django')

