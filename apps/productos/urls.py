from django.urls import path
from .views import *

app_name = 'productos'

urlpatterns=[
    path('registrar/', registrar_view, name = 'registrar'),
    path('consultar/', consultarProdutos_view, name = 'consultar'),
    path('subcategoria/<int:subcategoria_id>', consultarPorSubcategoria_view, name = 'consultarPorSubcategoria'),
    path('categoria/<int:categoria_id>', consultarPorCategoria_view, name = 'consultarPorCategoria'),
    path('producto/<str:codigo>', consultarProducto_view, name = 'consultarProducto'),
    path('modificar/<str:codigo>', modificarProductos_view, name = 'modificar'),
    path('eliminar/<str:codigo>', eliminarProducto_view, name = 'eliminar'),
    path('detalle/<int:id>', eliminarDetalle_view, name = 'eliminar_detalle'),
]