from django import forms

class CrearProyecto(forms.Form):
    nombre=forms.CharField(max_length=40)
    localizacion= forms.CharField(max_length=40)
    fecha= forms.DateField()

class CrearExperiencia(forms.Form):
    nombre=forms.CharField(max_length=40)
    fechainicio= forms.DateField()
    fechafin= forms.DateField()
    descripcion=forms.CharField(max_length=1000)

class CrearCursos(forms.Form):
    nombre=forms.CharField(max_length=40)
    institucion=forms.CharField(max_length=40)
    fechainicio= forms.DateField()
    fechafin= forms.DateField()
