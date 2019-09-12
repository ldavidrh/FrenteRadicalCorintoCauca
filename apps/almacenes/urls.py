from django.urls import path
from apps.almacenes.views import *

app_name = 'almacenes'

urlpatterns = [
    path('crear_almacen/', crear_almacen_view, name='crear_almacen'),
    path('consultar_almacenes/', consultar_almacenes_view, name='consultar_almacenes'),
    path('modificar_almacen/<int:id>', modificar_almacen_view, name='modificar_almacen'),
    path('eliminar_almacen/<int:id>', eliminar_almacen_view, name='eliminar_almacen'),
]