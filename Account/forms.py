from django import forms

from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

from django import forms
from avatar.forms import AvatarForm
from .models import User



class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")


class ProfileForm(forms.ModelForm):
    avatar = AvatarForm()

    class Meta:
        model = User
        fields = ['username', 'email', 'avatar']




class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=30)
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio


class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    
    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio



