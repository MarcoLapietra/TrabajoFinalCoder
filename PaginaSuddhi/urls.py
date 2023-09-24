from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cuidado_corporal', cuidado_corporal, name="CuidadoCorporal"),
    path('tinturas', tinturas_madre, name="Tinturas"),
    path('cursos', cursos, name="Cursos"),
]