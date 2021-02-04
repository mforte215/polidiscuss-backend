from django.db import models
from django.db.models.deletion import CASCADE
from taggit.managers import TaggableManager


class Article(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(max_length=2000, blank=True)
    author = models.ForeignKey('auth.User', related_name='articles', default='', on_delete=models.CASCADE)
    image_url = models.CharField(max_length=250, blank=True)
    subtitle = models.CharField(max_length=50, blank=True)
    tags = TaggableManager()


    class Meta:
        ordering = ['createdAt']