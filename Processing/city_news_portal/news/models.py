from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='articles')

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.article}'

class BannedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    banned_until = models.DateTimeField(null=True, blank=True)

    def is_banned(self):
        return self.banned_until and self.banned_until > datetime.now()


class SiteSettings(models.Model):
    background_color = models.CharField(max_length=20, default="#ffffff")
    font_color = models.CharField(max_length=20, default="#000000")
    font_size = models.IntegerField(default=14)
