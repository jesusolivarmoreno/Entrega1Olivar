from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from AppLogin.forms import UserRegisterForm
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
    return render(request,"AppLogin/login.html", contexto)

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
    return render(request,"AppLogin/login.html", contexto)

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
    return render(request,"AppLogin/login.html", contexto)

#FIN DE FORMULARIO DE REGISTRO  CUSTOMIZABLE
    
        