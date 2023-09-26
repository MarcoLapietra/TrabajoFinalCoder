from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def crea_producto(req):
    if req.method == 'POST':

        ProductForm = ProductoFormulario(req.POST)

        if ProductForm.is_valid():

            datos = ProductForm.cleaned_data

            producto = Producto(nombre=datos["nombre"], tipo=datos["tipo"])
            producto.save()
            return render(req,"inicio.html", {"mensaje : Producto creado con exito"})
        else:
            return render(req,"inicio.html", {"mensaje : Error al crear el producto"})
    else:
        ProductForm = ProductoFormulario()
        return render(req, 'crea_producto.html', {"ProductForm":ProductForm})
    



def list_prod(req):
    producto = Producto.objects.all()
    return render(req, "productos.html", {"productos":producto})
    