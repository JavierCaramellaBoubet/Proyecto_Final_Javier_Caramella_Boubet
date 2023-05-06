"""
URL configuration for Account project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *

from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [
    
    path("", inicioApp, name="inicioApp"),
    
    path("login/", login_request, name="login"),
    #path("login/", LoginView.as_view(template_name="Account/login.html"), name="login"),
    #path("login/", login_request(template_name="Account/login.html"), name="login"),
    path("register/", register, name="register"),
    path('logout/', LogoutView.as_view(template_name="Account/logout.html"), name='logout'),
    #path('logout/', LogoutView.as_view(template_name="Posts/posts_page.html"), name='logout'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar')
    
    path('avatar/', include('avatar.urls')),
    
    
]