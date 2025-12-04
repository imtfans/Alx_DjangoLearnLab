from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse

class PostCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pass')
        self.other = User.objects.create_user(username='bob', password='pass')
        self.post = Post.objects.create(title='T', content='C', author=self.user)

    def test_list_view(self):
        resp = self.client.get(reverse('post-list'))
        self.assertEqual(resp.status_code, 200)

    def test_create_requires_login(self):
        resp = self.client.get(reverse('post-create'))
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username='alice', password='pass')
        resp = self.client.get(reverse('post-create'))
        self.assertEqual(resp.status_code, 200)

    def test_update_author_only(self):
        self.client.login(username='bob', password='pass')  # not author
        resp = self.client.get(reverse('post-update', kwargs={'pk': self.post.pk}))
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username='alice', password='pass')
        resp = self.client.get(reverse('post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)


# Create your tests here.
