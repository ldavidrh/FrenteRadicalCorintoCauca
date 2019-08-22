from django.urls import path
from apps.subcategorias.views import *

app_name = 'subcategorias'

urlpatterns=[
    path('crear_subcategoria/', crear_subcategoria_view, name = 'crear_subcategoria'),
    path('modificar_subcategoria/<int:id>', modificar_subcategoria_view, name = 'modificar_subcategoria'),
    path('eliminar_subcategoria/<int:id>', eliminar_subcategoria_view, name = 'eliminar_subcategoria'),
]