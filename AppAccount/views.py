from django.shortcuts import render

from .models import Usuario

# Create your views here.

@login_required
def crear_usuario(request):

    if request.method== "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario= Usuario()
            usuario.nombre = form.cleaned_data['nombre']
            usuario.email = form.cleaned_data['email']
            usuario.contrasena = form.cleaned_data['contrasena']
            usuario.save()
            form = UsuarioForm()

    else:
        form = UsuarioForm()

    usuario = Usuario.objects.all() #Usuarui.objects.filter(nombre__icontains="P").all()
    
    return render(request, "AppCoder/usuario.html", {"usuario": usuario, "form" : form}) 



