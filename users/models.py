from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#**************************************************************************************
#  REFERENCES
#  Title: <code_snippets/django tutorial>
#  Author: Corey Schafer
#  Date: Last Updated March 18 2017
#  Availability: https://github.com/CoreyMSchafer/code_snippets
#  Used for User Profile creation 
# Title: ....
#
#***************************************************************************************

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

        
