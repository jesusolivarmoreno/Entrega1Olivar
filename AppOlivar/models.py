from django.db import models

# Modelo para Proyectos
class Proyectos(models.Model):
    nombre=models.CharField(max_length=40)
    localizacion= models.CharField(max_length=40)
    fecha= models.DateField()
# Modelo para Experiencia
class Experiencia(models.Model):
    nombre=models.CharField(max_length=40)
    fechainicio= models.DateField()
    fechafin= models.DateField()
    descripcion=models.CharField(max_length=1000)
# Modelo para Cursos realizados
class Cursos(models.Model):
    nombre=models.CharField(max_length=40)
    institucion=models.CharField(max_length=40)
    fechainicio= models.DateField()
    fechafin= models.DateField()
