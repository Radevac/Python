from django.db import models

class Dictionary(models.Model):
    english_word = models.CharField(max_length=100, unique=True)
    french_translation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.english_word} - {self.french_translation}"

