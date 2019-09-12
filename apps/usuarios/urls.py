from django.urls import path
from apps.usuarios.views import *

app_name = 'gerentes'
urlpatterns=[
    path('registro/', registroGerente_view, name = 'registro'),
    path('consultar_gerente/', consultarGerentes_view, name = 'consulta'),
    path('modificar_gerente/<str:numero_documento>', modificarGerente_view, name = 'modificar'),
    path('eliminar_gerente/<str:numero_documento>', eliminarGerente_view, name = 'eliminar'),
    path('activar_gerente/<str:numero_documento>', activarGerente_view, name = 'activar'),
]

