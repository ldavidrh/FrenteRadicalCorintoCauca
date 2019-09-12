from django.urls import path
from apps.clientes.views import *
from django.contrib.auth.views import *

app_name = 'clientes'
urlpatterns=[
    path('registro/', registro_view, name = 'registro'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('perfil/<str:numero_documento>', perfil_view, name = 'perfil'),
    path('change-password/', change_password, name = 'change_password'),
    path('eliminar-cuenta/<str:numero_documento>', eliminarCuenta_view, name = 'eliminar-cuenta'),
    path('consultar_clientes/', consultarClientes_view, name = 'consulta'),
    path('activar_cliente/<str:numero_documento>', activarCliente_view, name = 'activar-cuenta'),
]
