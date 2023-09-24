from django.shortcuts import render
from .models import *
from django.http import HttpResponse



# Create your views here.

def inicio(req):
    return render(req, "inicio.html") 



def cuidado_corporal(req):
    return render (req, "cuidado_corporal.html")


def tinturas_madre(req):
    return render(req, "tinturas.html")

def cursos(req):
    return render(req, "cursos.html")
