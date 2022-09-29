from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django import forms
from django.contrib.auth.models import User
from AppLogin.models import Avatar

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name")
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(label="Modificar Email")
    first_name = forms.CharField(label="Modificar Primer nombre")
    last_name = forms.CharField(label="Modificar Segundo nombre")
    #password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    #password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name")
        #help_texts = {k:""for k in fields}

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = "__all__"