from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from Productos import models
from Productos.views import *


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cuidado_corporal', cuidado_corporal, name="CuidadoCorporal"),
    path('tinturas', tinturas_madre, name="Tinturas"),
    path('cursos', cursos, name="Cursos"),
    path('productos', todos_productos, name="Productos"),
    path('crea_producto', crea_producto, name ="CrearProd"),
    path('list_prod', list_prod, name ="ListProd"),
    path('login/', loginView, name="Login"),
    path('register/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editar-pefil/', editar_perfil, name="EditarPefil"),
    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),

]