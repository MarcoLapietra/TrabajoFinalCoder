from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from Productos.views import *
from Productos.models import *
from .forms import *
from PaginaSuddhi.models import Cliente
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden


# Create your views here.

    

@staff_member_required
def agregar_producto(request):
    if not request.user.is_authenticated or not request.user:
        
        return redirect('Inicio')

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        form = ProductoForm()

    return render(request, 'agregar_producto.html', {'form': form})






def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})




@staff_member_required  
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = EditarProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ListProd')
    else:
        form = EditarProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})




def aco_lav(req):
    return render(req, "acond_lavanda.html") 


def jab_arc(req):
    return render(req, "jabon_arcilla.html") 


def jab_esp(req):
    return render(req, "jabon_espirulina.html") 



def lub_nat(req):
    return render(req, "lubricante_natural.html") 


def prot_sol(req):
    return render(req, "protector_solar.html") 


def sha_sol(req):
    return render(req, "shampoo_solido.html") 


def ung_arn(req):
    return render(req, "unguento_arnica.html") 


def ung_can(req):
    return render(req, "unguento_canabis.html") 



@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    usuario=request.user
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:
            producto.delete()
            return redirect('ListProd')
    
    return render(request, 'eliminar_producto.html', {'producto': producto})