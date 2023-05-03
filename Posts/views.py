from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

from django.contrib import messages
from django.http import HttpResponse

from .forms import *

# Create your views here.

def home(request):
    posts = Post.objects.all() 
    context = {'posts':posts}
    return render(request, 'Posts/posts_page.html', context)   #El context contiene las variables que le enviaremos a TEMPLATES

def post(request, pk):
    post = Post.objects.get(id=pk)
    context={'post':post}
    return render(request, 'Posts/post.html',context)

def formulario(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')        

    context={'form':form}
    return render(request, 'Posts/form_post.html', context)

def deletePost (request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    context = {'post':post}

    return render(request,'delete_template.html', context)

def updatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    update = 1
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        form.save()
        return redirect('home')

    context = {"form":form, "update":update}
    return render(request,'Posts/form_post.html', context)


##########################################################################

def nuestraEmpresa(request):
    return render(request, 'nuestraEmpresa.html')


##########################################################################


#def buscarProducto(request):
#    return render(request, 'busquedaProducto.html')

def buscarBlog(request):
    return render(request, 'busquedaBlog.html')
 

    
def buscandoBlog(request):
    blogIngresado= request.GET["nombre"]
    if blogIngresado!="":
        blog=Post.objects.filter(nombre__icontains=blogIngresado)
        print(blog)
        return render(request, "resultadoBusquedaBlog.html", {"nombre": nombre})
    else:
        return render(request, "busquedaBlog.html", {"mensaje": "POR FAVOR INGRESA UN BLOG PARA BUSCAR!!!"})    