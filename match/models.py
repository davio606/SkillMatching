from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username