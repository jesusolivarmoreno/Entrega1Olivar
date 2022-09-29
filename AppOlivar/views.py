from http.client import HTTPResponse
from this import d
from urllib import request
from django.shortcuts import render, redirect
from AppOlivar.models import Proyectos, Experiencia , Cursos
from django.contrib import messages


from AppOlivar.forms import *
 
# Create your views here.


# creando funicon de Vista para ELIMINAR 

def Eliminarexperiencia(request,id):
    eliminar_experiencia = Experiencia.objects.get(id=id)
    if eliminar_experiencia.delete():
        messages.info(request,f"La experiencia ha sido eliminada correctamente")
        return redirect("AppOlivarPortFolioItem")
    else:
        messages.error(f"Algo salio mal")
        return redirect("AppOlivarContact")
    
# FIN ELIMINAR 

# CREANDO FUNCION DE VISTA PARA EDITAR 

def Editarexperiencia(request,id):
    editar_experiencia = Experiencia.objects.get(id=id)
    if request.method == 'POST':
        formulario_experiencia = CrearExperiencia(request.POST)
        if formulario_experiencia.is_valid():
            data = formulario_experiencia.cleaned_data
            editar_experiencia.nombre = data.get('nombre')
            editar_experiencia.fechainicio = data.get('fechainicio')
            editar_experiencia.fechafin = data.get('fechafin')
            editar_experiencia.descripcion = data.get('descripcion')
            
            editar_experiencia.save()
            messages.success(request,f"La experiencia ha sido Actualizado correctamente")
            return redirect("AppOlivarPortFolioItem")
    
    contexto = {
        "formexperiencia" :CrearExperiencia(
           initial= {
               "nombre": editar_experiencia.nombre,  
                "fechainicio": editar_experiencia.fechainicio,
                 "fechafin": editar_experiencia.fechafin, 
                 "descripcion": editar_experiencia.descripcion 
           } 
            
        )
    }
    return render(request,"AppOlivar/blog-post.html",contexto)

# Vista para el HTML 

def Inicio(request):
    return render(request, "index.html")

def About(request):
    return render(request, "AppOlivar/about.html")

def Contact(request):
    return render(request, "AppOlivar/contact.html")

def Pricing(request):
    return render(request, "AppOlivar/pricing.html")

def Faq(request):
    return render(request, "AppOlivar/faq.html")

# FIN vista HTML

# Vista para Formularios

# Comienzo Formulario Proyectos
def formulario_proyecto(request):
    if request.method == 'POST':
        formulario_proyecto = CrearProyecto(request.POST)
        if formulario_proyecto.is_valid():
            data = formulario_proyecto.cleaned_data
            create_proyecto = Proyectos(nombre=data.get("nombre"), localizacion=data.get("localizacion"),fecha=data.get("fecha"))
            create_proyecto.save()
            return redirect("AppInicio")
        else:
            return redirect("AppOlivarContact")
    contexto = {
        "formproyecto": CrearProyecto()
    }
    return render(request,"AppOlivar/blog-home.html",contexto)
#Fin Formulario Proyectos

#Comienzo Formulario Experiencia

def formulario_experiencia(request):
    if request.method == 'POST':
        formulario_experiencia = CrearExperiencia(request.POST)
        if formulario_experiencia.is_valid():
            data = formulario_experiencia.cleaned_data
            create_experiencia = Experiencia(nombre=data.get("nombre"), fechainicio=data.get("fechainicio"),fechafin=data.get("fechafin"), descripcion=data.get("descripcion"))
            create_experiencia.save()
            messages.success(request,f"La experiencia ha sido creada correctamente")
            return redirect("AppInicio")
        else:
            messages.error(request,f"UPS! Algo salio mal")
            return redirect("AppOlivarContact")
    contexto = {
        "formexperiencia": CrearExperiencia()
    }
    return render(request,"AppOlivar/blog-post.html",contexto)

#Fin Formulario Experiencia

#Comienzo Formulario Cursos

def formulario_cursos(request):
    if request.method == 'POST':
        formulario_cursos = CrearCursos(request.POST)
        if formulario_cursos.is_valid():
            data = formulario_cursos.cleaned_data
            create_cursos = Cursos(nombre=data.get("nombre"), institucion=data.get("institucion"),fechainicio=data.get("fechainicio"), fechafin=data.get("fechafin"))
            create_cursos.save()
            return redirect("AppInicio")
        else:
            return redirect("AppOlivarContact")
    contexto = {
        "formcursos": CrearCursos()
    }
    return render(request,"AppOlivar/portfolio-overview.html",contexto)

#Fin Formulario Cursos

# Comienzo de Vista Experiencia
#ESTE PORTAFOLIO ITEM ES SOLO PARA LLAMAR A LA BASE DE DATOS 
def PortFolioItem(request):
    vistaexperiencia = Experiencia.objects.all()

    contexto ={
        "formexperiencias" : Busquedaexperienciaform(),
        "verexperiencia": vistaexperiencia  
    }
    
    return render(request,"AppOlivar/portfolio-item.html",contexto)
# FIN de vista experiencia
# FIN PORTAFOLIO ITEM



#Busqueda Experiencias
#ESTE PARA BOTON DE BUSQUEDA MAS ESPECIFICAS
def Busquedaexperiencia_get(request):
    nombre = request.GET.get('nombre')
    experiencias = Experiencia.objects.filter(nombre__icontains=nombre)
    contexto = {
        "formexperiencias" : Busquedaexperienciaform(),
        "verexperiencia" : experiencias 
    }
    return render(request, "AppOlivar/portfolio-item.html",contexto)
#FIN BUSQUEDA EXPERIENCIA

# ESTA ES LA ORIGINAL 
#def Busquedaexperiencia(request):    
#    contexto = {
#        "formexperiencias" : Busquedaexperienciaform() 
#    }
#    return render(request, "AppOlivar/busquedaexperiencia.html",contexto)
#ESTA ES EL FIN DE LA ORIGINAL

#FIN BUSQUEDA EXPERIENCIA