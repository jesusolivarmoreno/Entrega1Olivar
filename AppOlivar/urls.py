"""Entrega1Olivar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from AppOlivar import views
from AppOlivar.views import Busquedaexperiencia_get, Inicio, About , Contact , Pricing , Faq , PortFolioItem , formulario_proyecto , formulario_experiencia , formulario_cursos
urlpatterns = [
    path('', Inicio, name="AppInicio"),
    path('about', About, name="AppOlivarAbout"),
    path('contact', Contact, name="AppOlivarContact"),
    path('pricing', Pricing, name="AppOlivarPricing"),
    path('faq', Faq, name="AppOlivarFaq"),
    path('bloghome', formulario_proyecto, name="AppOlivarBlogHome"),
    path('blogpost', formulario_experiencia, name="AppOlivarBlogPost"),
    path('portfoliooverview', formulario_cursos, name="AppOlivarPortFolioOverview"),
    path('portfolioitem', PortFolioItem, name="AppOlivarPortFolioItem"),
    #path('busquedaexperiencia', Busquedaexperiencia, name="AppOlivarBusquedaExperiencia"),
    path('busquedaexperiencia_get', Busquedaexperiencia_get, name="AppOlivarBusquedaExperienciaget"),
]
