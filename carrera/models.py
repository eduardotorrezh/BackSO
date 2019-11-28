from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    director = models.CharField(max_length=50)

    # usuario = models.CharField(max_length=30)
    # correo = models.EmailField(max_length = 254) 
    # contraseña = models.CharField(max_length=20)

