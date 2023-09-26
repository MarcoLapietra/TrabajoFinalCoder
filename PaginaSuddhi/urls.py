from django.urls import path
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
    path('list_prod', list_prod, name ="ListProd")

]