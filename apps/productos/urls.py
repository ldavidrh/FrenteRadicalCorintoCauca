from django.urls import path
from .views import *

app_name = 'productos'

urlpatterns=[
    path('registrar/', registrar_view, name = 'registrar'),
    path('consultar/', consultarProdutos_view, name = 'consultar'),
    path('consultar/<int:subcategoria_id>', consultarPorSubcategoria_view, name = 'consultarPorSubcategoria'),
    path('producto/<str:codigo>', consultarProducto_view, name = 'consultarProducto'),
    path('modificar/<str:codigo>', modificarProductos_view, name = 'modificar'),
    path('eliminar/<str:codigo>', eliminarProducto_view, name = 'eliminar'),
]