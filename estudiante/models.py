from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.CharField(max_length=3)
    sexo = models.CharField(max_length=7)
    direccion = models.CharField(max_length=50)
    carrera = models.CharField(max_length=18)
