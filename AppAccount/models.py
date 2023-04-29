from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre= models.CharField('Nombre', max_length=12)
    email= models.EmailField('E-mail')
    contrasena= models.CharField('Contraseña', max_length=12)

    def __str__(self):
        return f"{self.nombre} {self.email} {self.contrasena}" 
    


class Blog(models.Model):
    titulo= models.CharField('Título del Blog', max_length=150, unique= True) 
    subtitulo= models.CharField('SubTítulo del Blog', max_length=150, unique= True) 
    cuerpo= models.TextField('Texto/Descripción', max_length=10000)
    autor= models.CharField('Autor', max_length=50)
    imagen= models.ImageField()
    publicado= models.BooleanField('Publicado / No Publicado', default= False)
    fecha_publicado= models.DateField('Fecha de Publicación')


class Mensaje(models.Model):
    nombre= models.CharField(max_length=12)
    cuerpo= models.CharField(max_length=10000)
    fecha= models.DateField()
    entregado= models.BooleanField()

    