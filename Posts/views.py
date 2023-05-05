from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect 

from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF  
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases CLASS 

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


#@login_required
def formulario(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')        

    context={'form':form}
    return render(request, 'Posts/form_post.html', context)


#@login_required
def deletePost (request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    context = {'post':post}

    return render(request,'delete_template.html', context)


#@login_required
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

###########################################################################

#@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect("")
    else:
        form = CommentForm() # asignar una instancia del formulario vacío

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})




##########################################################################

def nuestraEmpresa(request):
    return render(request, 'nuestraEmpresa.html')


##########################################################################


def buscarBlog(request):
    return render(request, 'Posts/busquedaBlog.html')
 

"""
   
def buscandoBlog(request):
    blogIngresado= request.GET["nombre"]
   
    if blogIngresado!="":
            
        blog=Post.objects.filter(blogingresado__incontains = blogIngresado)
        print(blog)
        return render(request, "resultadoBusquedaBlog.html", {"nombre": blog})        
        
    else:
        return render(request, "busquedaBlog.html", {"mensaje": "POR FAVOR INGRESA UN BLOG PARA BUSCAR!!!"})    

"""


        
def buscandoBlog(request):
    
    nombre= request.GET["nombre"]
    if nombre!="":
            
        nombre=Post.objects.filter(title__icontains = nombre)
        print(nombre)
        return render(request, "Posts/resultadoBusquedaBlog.html", {"nombre": nombre})
             
    else:
        
        return render(request, "Posts/busquedaBlog.html", {"mensaje": "POR FAVOR INGRESA UN BLOG PARA BUSCAR!!!"})   
    


def search(request):
    
    nombre= request.GET["nombre"]
    if nombre!="":
            
        nombre=Post.objects.filter(title__icontains = nombre)
        print(nombre)
        return render(request, "Posts/resultadoBusquedaBlog.html", {"nombre": nombre})
             
    else:
        
        return render(request, "Posts/busquedaBlog.html", {"mensaje": "POR FAVOR INGRESA UN BLOG PARA BUSCAR!!!"})  



#########################################################################################