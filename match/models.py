from django.db import models
from datetime import datetime
# Create your models here.


class Message(models.Model):
    sender = models.CharField(max_length=200)
    reciever = models.CharField(max_length=200)
    message_content = models.CharField(max_length=5000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    subject = models.CharField(max_length=1000, default='Message Subject')
