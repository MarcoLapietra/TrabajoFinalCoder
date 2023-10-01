from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
from Productos import models
from Productos.views import *



urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cuidado_corporal', cuidado_corporal, name="CuidadoCorporal"),
    path('tinturas', tinturas_madre, name="Tinturas"),
    path('cursos', cursos, name="Cursos"),
    path('productos', todos_productos, name="Productos"),
    #path('crea_producto', crea_producto, name ="CrearProd"),
    #path('list_prod', list_prod, name ="ListProd"),
    path('login/', inicio_sesion, name="Login"),
    path('register/', registro, name="Registrar"),
    path('logout/', cerrar_sesion, name="Logout"),
    path('eliminar_cuenta/', eliminar_cuenta, name='eliminar_cuenta'),
    path('editar-pefil/', editar_perfil, name="EditarPefil"),
    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),
    path('about/', about, name="About"),
    path('contacto/', contacto, name='Contacto'),
    path('buscar/', buscar, name="Buscar"),
    path('acondicionador_lavanda/', aco_lav, name="AcoLav"),
    path('jabon-arc/', jab_arc, name="JabArc"),
    path('jabon-esp/', jab_esp, name="JabEsp"),
    path('lubricante_nat/', lub_nat, name="LubNat"),
    path('protector-solar/', prot_sol, name="ProtSol"),
    path('shampoo-solido/', sha_sol, name="ShmpSol"),
    path('unguento-arnica/', ung_arn, name="UngAr"),
    path('unguento-can/', ung_can, name="UngCan"),
    path('login_error/', ung_can, name="UngCan"),
    path('agregar_producto/', agregar_producto, name="AgregaProd"),
    path('listar_productos/', listar_productos, name='ListProd'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)