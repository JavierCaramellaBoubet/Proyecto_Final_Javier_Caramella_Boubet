from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)


        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['subtitulo'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagen_portada'].widget.attrs.update({'class': 'form-control'})