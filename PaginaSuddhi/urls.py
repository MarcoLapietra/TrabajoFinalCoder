from django.urls import path, include
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
    path('login/', inicio_sesion, name="Login"),
    path('register/', registro, name="Registrar"),
    path('logout/', cerrar_sesion, name="Logout"),
    path('eliminar_cuenta/', eliminar_cuenta, name='eliminar_cuenta'),
    path('editar-pefil/', editar_perfil, name="EditarPefil"),
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
    path('detalle_producto/<int:producto_id>/',detalle_producto, name='detalle_producto'),
    path('editar_producto/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('avatar/', include('avatar.urls')),
    path('admin_contact_requests/', admin_ver_mensajes_de_contacto, name='admin_contact_requests'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


