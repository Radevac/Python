from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    office_number = models.CharField(max_length=10)
    skype = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name} - {self.position}"

