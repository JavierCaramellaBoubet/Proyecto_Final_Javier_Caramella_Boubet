from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import AbstractUser
from avatar.models import Avatar

# Create your models here.



class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    #para usar imagenes voy a tener que installar Pillow. de que manera?  pip install Pillow


class User(AbstractUser):
    # ... otros campos del modelo ...
    avatar = models.OneToOneField(Avatar, on_delete=models.CASCADE, null=True, blank=True)    