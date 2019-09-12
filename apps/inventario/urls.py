from django.urls import path
from .views import *

app_name='inventario'

urlpatterns=[
    path('modificar/<int:id>', actualizarCantidad_view, name = 'modificar'),
]