from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=30)
    correo = models.EmailField(max_length = 254) 
    contraseña = models.CharField(max_length=30)

