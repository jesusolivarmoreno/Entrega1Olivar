from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from AppLogin.forms import AvatarForm, UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from AppLogin.models import Avatar
# Create your views here.
#Creacion del Login usa el ususario y contrasena de la administracion Django
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get("username")
            contra = data.get("password")
            user = authenticate(username=usuario,password=contra)
            if user:
                login(request,user)
                messages.info(request, "Inicio de sesion satisfactorio")
            else:
                messages.info(request, "Inicio de sesion fallido!")
        else:
            messages.info(request, "Inicio de sesion fallido!")
        return redirect("AppInicio")

    contexto = {
        "form": AuthenticationForm(),
        "nombre_formulario": "Login" 
    }
    return render(request,"AppLogin/base_formulario.html", contexto)

#Fin de la Creacion 
####################################
####################################

#Comienzo del Registro este metodo se hace con el por default de Django

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Su usuario ha sido registrado correctamente")
        else:
            messages.info(request, "Tu usuario no pudo ser registrado!")
        return redirect("AppInicio")   
    contexto = {
        "form": UserCreationForm(),
        "nombre_formulario": "Registro" 
        #"form": UserRegisterForm(),

    }
    return render(request,"AppLogin/base_formulario.html", contexto)

#FIN DE FORMULARIO DE REGISTRO  POR DEFAULT
#######################################################
#######################################################
######################################################
#Comienzo del Registro este metodo se hace para Customizable

def register_custom(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Su usuario ha sido registrado correctamente")
        else:
            messages.info(request, "Tu usuario no pudo ser registrado!")
        return redirect("AppInicio")   
    contexto = {
        "nombre_formulario": "Registro", 
        "form": UserRegisterForm(),

    }
    return render(request,"AppLogin/base_formulario.html", contexto)

#FIN DE FORMULARIO DE REGISTRO  CUSTOMIZABLE
##############################################
##############################################
#############################################

#Edicion de Profile Usuario Django

@login_required
def editar_usuario(request):
    usuario= request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            usuario.username = data["username"]
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.save()
            messages.info(request, "Su usuario ha sido actualizado correctamente")
        else:
            messages.info(request, "Tu usuario no pudo ser Actualizado!")
        return redirect("AppInicio")
    contexto = {
        "nombre_formulario": "Actualizar", 
        "form": UserEditForm(
            initial={
                "username": usuario.username,
                "email": usuario.email,
                "first_name": usuario.first_name,
                "last_name": usuario.last_name
            }),
    }
    return render(request,"AppLogin/base_formulario.html", contexto)

### Editar el Avatar 
####
@login_required
def upload_avatar(request):
    if request.method == "POST":        
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            data= form.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("usuario"))
            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = form.cleaned_data["imagen"]
                avatar.save()
            else:
                avatar = Avatar(user=data.get("user"), imagen=data.get("imagen"))
                avatar.save()
        return redirect("AppInicio")
    contexto = {
        "nombre_formulario": "Crear", 
        "form": AvatarForm()
    }
    return render(request,"AppLogin/avatar.html", contexto)
    
              
            