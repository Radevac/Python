from django.db import models

from django.db import models

class BasketballPlayer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    height = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.height} см"

