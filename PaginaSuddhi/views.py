from django.shortcuts import render
from .models import *
from django.http import HttpResponse



# Create your views here.

def inicio(req):
    return render(req, "inicio.html") 
