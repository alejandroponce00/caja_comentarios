from django import forms
class CreateComentario(forms.Form):
     nombre=forms.CharField(label="nombre", max_length=200)
     mensaje=forms.CharField(label = "ingrese su comentario" ,widget=forms.Textarea)   