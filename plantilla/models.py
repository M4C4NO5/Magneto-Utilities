from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class TemplateModel(models.Model):
    name = models.CharField(max_length=40)
    font = models.CharField(max_length=40,null=False)
    font_size = models.IntegerField(null=False)
    color = models.CharField(max_length=30, null=False)


    
    
    