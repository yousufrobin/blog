from email.policy import default
from django.db import models
from datetime import datetime


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=120)
    body = models.CharField(max_length=1000000)
    created_time = models.DateTimeField(default=datetime.now, blank=True)
