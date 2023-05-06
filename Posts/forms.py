from django.forms import ModelForm
from django import forms
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)


        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['subtitulo'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagen_portada'].widget.attrs.update({'class': 'form-control'})
        #self.fields['fecha_creacion'].widget.attrs.update({'class': 'form-control'})





#class CommentForm(ModelForm):
#    class Meta:
#        model= Comment
#        fields= ('name','email','content','active')     



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        #self.fields['active'].widget.attrs.update({'class': 'form-control'})        





