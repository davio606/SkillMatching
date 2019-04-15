from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#User and Profile have one to one relation. If a user is deleted, then profile is deleted
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    major = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    numLikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if(img.height > 300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
""" 
class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=1024)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    team = models.ForeignKey('Team', on_delete=models.PROTECT) """

        
