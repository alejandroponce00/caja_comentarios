from django.shortcuts import render
from .forms import CreateComentario

def caja_coment(request):
    
    form = CreateComentario
    
    if request.method == "POST":
            print(request.POST)
            
    return render(request, 'coment.html' ,{'form' : form}) 