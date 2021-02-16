from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class User(AbstractUser):
    pass

class Article(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    content = RichTextField()
    author = models.ForeignKey('articles.User', related_name='articles', default='', on_delete=models.CASCADE)
    image_url = models.URLField()
    subtitle = models.CharField(max_length=50, blank=True)
    tags = TaggableManager()

    def __str__(self):
        selfString = self.title + " by " + self.author.first_name + " " + self.author.last_name

        return selfString


    class Meta:
        ordering = ['createdAt']

class Post(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    content = RichTextField()
    poster = models.ForeignKey('posts.User', related_name='posts', default='', on_delete=models.CASCADE)
    image_url = models.URLField()
    subtitle = models.CharField(max_length=50, blank=True)
    tags = TaggableManager()

    def __str__(self):
        selfString = self.title + " by " + self.author.first_name + " " + self.author.last_name

        return selfString


    class Meta: 
        ordering = ['createdAt']