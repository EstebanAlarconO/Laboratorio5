from django.db import models

# Create your models here.

class Informacion(models.Model):
    ip = models.CharField(max_length=255)
    so = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    contrasenia = models.CharField(max_length=255)