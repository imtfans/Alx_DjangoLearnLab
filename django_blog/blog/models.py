from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Post'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Author'
    )
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})
    
