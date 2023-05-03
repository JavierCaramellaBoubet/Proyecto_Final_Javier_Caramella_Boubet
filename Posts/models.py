from django.db import models
import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, null=True, blank= True)
    description = RichTextUploadingField(null=True, blank= True)
    imagen_portada = models.ImageField(null=True, blank=True, default = "default-image.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) #Para asignar un ID aleatorio
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return self.title
    

    def __str__(self):
        texto = "{0} ({1})({2})"
        return texto.format(self.title,self.subtitulo,self.fecha_creacion)