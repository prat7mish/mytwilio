from django.db import models

# Create your models here.
class Post(models.Model):
    number = models.CharField(max_length=120)