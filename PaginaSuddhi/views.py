from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse
from Productos.views import *
from Productos.models import *
from .forms import *


# Create your views here.

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




#Login


def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}!"})
            
        return render(req, "inicio.html", {"mensaje": f"Datos incorrectos"})
    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})

def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        return render(req, "inicio.html", {"mensaje": f"Formulario invalido"})
            
    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})

def editar_perfil(req):

    usuario = req.user
    if req.method == 'POST':

        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "inicio.html", {"mensaje": "Datos actualizados con éxito!"})
        else:
            return render(req, "editarPerfil.html", {"miFormulario": miFormulario})

    else:
        miFormulario = UserEditForm(instance=usuario)
        return render(req, "editarPerfil.html", {"miFormulario": miFormulario})
    
def crea_cliente(req):

    if req.method == 'POST':

        info = req.POST

        miFormulario = ClienteFormulario({
            "nombre": info["nombre"],
            "apellido": info["apellido"],
            "email": info["email"]
        })
        userForm = UserCreationForm({
            "username": info["username"],
            "password1": info["password1"],
            "password2": info["password2"]
        })

        if miFormulario.is_valid() and userForm.is_valid():

            data = miFormulario.cleaned_data
            data.update(userForm.cleaned_data)

            user = User(username=data["username"])
            user.set_password(data["password1"])
            user.save()

            estudiante = Cliente(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], user=user)
            estudiante.save() 

            return render(req, "inicio.html", {"mensaje": "Estudiante creado con éxito!"})
    else:

        miFormulario = ClienteFormulario()
        userForm = UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario, "userForm": userForm})
    


def agregar_avatar(req):

    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            avatar = Avatar(user=req.user, imagen=data["imagen"])

            avatar.save()

            return render(req, "inicio.html", {"mensaje": "Avatar actualizados con éxito!"})

    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregarAvatar.html", {"miFormulario": miFormulario})
        
        return render(req, "registro.html", {"miFormulario": miFormulario})
    


    
