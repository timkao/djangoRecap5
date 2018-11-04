from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse

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
    response = self.client.get('/post/1/')
    no_response = self.client.get('/post/10000/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)

  def test_post_create_view(self):
    response = self.client.post(reverse('postNew'), {
      'title': 'New title',
      'author': self.user,
      'body': 'New text',
    })
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'New title')

  def test_post_edit_view(self):
    response = self.client.post(reverse('postEdit', args='1'), {
      'title': 'Update title',
      'body': 'Update text',
    })
    self.assertEqual(response.status_code, 302)

  def test_post_delete_view(self):
    response = self.client.get(reverse('postDelete', args='1'))
    self.assertEqual(response.status_code, 200)

