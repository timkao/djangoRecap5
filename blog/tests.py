from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

from .models import Post

class BlogTests(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username = 'testuser',
      email = 'test@email.com',
      password = 'secret'
    )

    self.post = Post.objects.create(
      title='A good title',
      body='nice body content',
      author=self.user
    )

  def test_string_representation(self):
    post = Post(title='a sample title')
    self.assertEqual(str(post), post.title)

  def test_post_detail_view(self):
    response = self.client.get('/post/1')
    no_response = self.client.get('/post/10000')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)

