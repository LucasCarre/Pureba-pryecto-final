from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Practicas(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_la_practica = models.DateField()
    realizada = models.BooleanField()

class Sugerencias(models.Model):
    nombre_del_curso = models.CharField(max_length=40)
    modalidad = models.CharField(max_length=40)