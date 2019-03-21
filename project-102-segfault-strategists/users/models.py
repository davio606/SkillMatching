from django.db import models
from django.contrib.auth.models import User

#User and Profile have one to one relation. If a user is deleted, then profile is deleted
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'