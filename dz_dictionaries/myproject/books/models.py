from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField()
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"

