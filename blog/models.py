from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
   username = models.CharField(max_length=100)
   title = models.CharField(max_length=3, widget=models.Select(choices=TITLE_CHOICES),)
   date = models.DateField(required=False)