from django.db import models
import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, null=True, blank= True)
    description = RichTextUploadingField(null=True, blank= True)
    imagen_portada = models.ImageField(null=True, blank=True, default = "{% static 'images/cliente_feliz.jpg' %}")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) #Para asignar un ID aleatorio
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return self.title
    

    def __str__(self):
        texto = "{0} ({1})({2})"
        #texto = "{0} ({1})({2})({3})({4})({5})"
        return texto.format(self.title,self.subtitulo,self.fecha_creacion)
        #return texto.format(self.title,self.subtitulo,self.description,self.imagen_portada,self.id,self.fecha_creacion)



class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments') 
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    content= models.TextField()
    active= models.BooleanField(default=False)

    def __str__(self):        
        #texto = "{0} ({1})"        
        #return texto.format(self.name,self.content)
    
        return f"Comentario de: {self.name} , {self.content}" 
   

