from django.db import models

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Theme(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Poem(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    content = models.TextField()
