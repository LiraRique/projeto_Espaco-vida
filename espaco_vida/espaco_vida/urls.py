
from django.contrib import admin
from django.urls import path
from WEB.views import *

urlpatterns = [
    #PAGINAS DAS HOMES
    path('', login),
    path('deash_usuario/',deash_usuario),
    path('formulario_cadastro/',formulario_cadastro),
]