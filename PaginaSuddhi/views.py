from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from Productos.views import *
from Productos.models import *
from .forms import *


# Create your views here.
#
#Parte Usuarios
#


def registro(request):
    if request.method == 'POST':
        user_form = RegistroForm(request.POST)
        
        if user_form.is_valid():
            
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            
            login(request, user)
            
            return redirect('Inicio')  

    else:
        user_form = RegistroForm()
    
    return render(request, 'registro.html', {'user_form': user_form})



def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Inicio')
        else:
            messages.error(request, 'Inicio de sesión fallido. Por favor, verifica tus credenciales.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return render(request, template_name='inicio.html')





@login_required
def editar_perfil(request):
    perfil_cliente = None 

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            usuario = miFormulario.save(commit=False)
            usuario.set_password(miFormulario.cleaned_data["password1"])
            usuario.save()

            if hasattr(usuario, 'cliente'):
                perfil_cliente = usuario.cliente

            return redirect('Inicio')
        else:
            return render(request, "editarperfil.html", {"miFormulario": miFormulario})
    else:
        miFormulario = UserEditForm(instance=request.user)

        if hasattr(request.user, 'cliente'):
            perfil_cliente = request.user.cliente

    return render(request, "editarperfil.html", {"miFormulario": miFormulario, "perfil_cliente": perfil_cliente})



@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada exitosamente.')
        return redirect('Inicio') 
    return render(request, 'eliminar_cuenta.html')
    






def inicio(req):
    return render(req, "inicio.html")




def cuidado_corporal(req):
    return render (req, "cuidado_corporal.html")


def tinturas_madre(req):
    return render(req, "tinturas.html")

def cursos(req):
    return render(req, "cursos.html")



def todos_productos(req):
    return render(req,"vista_productos.html")

def about(req):
    return render(req,"about.html")


def contacto(req):
    return render(req,"contacto.html")







def buscar(request):
    query = request.GET.get('q')
    productos = []

    if query:
        productos = Producto.objects.filter(titulo__icontains=query)

    return render(request, 'busqueda.html', {'productos': productos, 'query': query})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})




def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})





@login_required
def contacto(req):
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            ContactRequest.objects.create(
                user=req.user,
                nombre=nombre,
                correo=correo,
                telefono=telefono,
                subject=subject,
                message=message
            )
            messages.success(req, 'Tu solicitud de contacto ha sido enviada de forma exitosa.')
            return redirect('Contacto')
    else:
        form = ContactForm()

    return render(req, 'contact.html', {'form': form})





def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin, login_url='login.html')
def admin_ver_mensajes_de_contacto(req):
    contact_requests = ContactRequest.objects.all()
    return render(req, 'admin_contact_requests.html', {'contact_requests': contact_requests})







