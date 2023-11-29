"""Models for the application 'blogs' """
from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2450)
