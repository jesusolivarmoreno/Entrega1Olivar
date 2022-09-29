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
    def __str__(self):
        return f"Empresa : {self.nombre}, Fecha de Inicio : {self.fechainicio}, Fecha de culminacion : {self.fechafin}, Descripcion : {self.descripcion}"
        return super().__str__()
# Modelo para Cursos realizados
class Cursos(models.Model):
    nombre=models.CharField(max_length=40)
    institucion=models.CharField(max_length=40)
    fechainicio= models.DateField()
    fechafin= models.DateField()
