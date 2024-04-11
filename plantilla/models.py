from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver

# Create your models here.
class Plantilla(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    titulo = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=100, null=False)
    URL = models.URLField(blank=True)
    fuente = models.CharField(max_length=40,null=False)
    tamaña_fuente = models.IntegerField(null=False)
    color = models.CharField(max_length=30, null=False)
    disposicion = models.BooleanField(default=False)

class Vacante(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    dimension = models.CharField(max_length=25, null=False)
    formato = models.CharField(max_length=10, null=True)
    plantilla_id = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
    
    
    