from django.shortcuts import render
from .models import Avatar
from .forms import RegistroUsuarioForm, UserEditForm, AvatarForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF  
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases CLASS   

# Create your views here.


    
def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatars/avatarpordefecto.png"



def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")


def inicioApp(request):

    return render(request, "Account/inicio.html", {"avatar":obtenerAvatar(request)})


# vistas basadas en clases:



#login logout register

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            info = form.cleaned_data

            usu = info["username"]
            clave = info["password"]
            # verifica si el usuario existe, si existe, lo devuelve, y si no devuelve None
            usuario = authenticate(username=usu, password=clave)

            if usuario is not None:
                login(request, usuario)
                return render(request, "Account/main.html", {"mensaje": f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "Account/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "Account/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
    else:
        form = AuthenticationForm()
        return render(request, "Account/login.html", {"form": form})





def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "Account/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "Account/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "Account/register.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "Account/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "Account/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "Account/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])#antes de guardarlo, tengo q hacer algo
            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "Account/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "Account/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "Account/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})
