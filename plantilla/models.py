from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class TemplateModel(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=30, null=False, default='N/A')
    desc = models.CharField(max_length=40, null=False, default='N/A')
    url = models.URLField(max_length=100, null=True)
    color = models.CharField(max_length=30, null=False, default='N/A')


    
    
    