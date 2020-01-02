from django.shortcuts import render
from django.http import HttpResponse

############## PAGINAS DAS HOMES ##############

def login(request):
    return render(request,'login.html')

def deash_usuario(request):
    return render(request,'deash_usuario.html')

def formulario_cadastro(request):
    return render(request,'formulario_cadastro.html')