from django.urls import path
from apps.carritos.views import *
from django.contrib.auth.views import *

app_name = 'carritos'

urlpatterns = [
    path('addToCart/<str:codigo>', addToCart_view, name='addToCart'),
    path('carrito', consultarCarrito_view, name='carrito'),
    path('carrito/<int:id>', eliminarCarrito_view, name='eliminar'),
    path('sumarCantidad/<int:id>', cambiarCantidad_view, name='modificar'),
]