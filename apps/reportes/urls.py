from django.urls import path
from .views import *

app_name='reportes'

urlpatterns= [
    path('productos_mas_vendidos/', productos_mas_vendidos, name = 'productos_mas_vendidos'),
    path('productos_menos_vendidos/', productos_menos_vendidos, name = 'productos_menos_vendidos'),
    path('ventas_por_fecha/', ventas_por_fecha, name = 'ventas_por_fecha'),
    path('ventas_producto_ultimos_meses/', ventas_producto_ultimos_meses, name = 'ventas_producto_ultimos_meses'),
    path('productos_baja_existencia/', productos_baja_existencia, name = 'productos_baja_existencia'),
    path('aniversarios_mes_siguiente/', aniversarios_mes_siguiente, name = 'aniversarios_mes_siguiente'),
    path('mayor_ingreso_dinero/', mayor_ingreso_dinero, name = 'mayor_ingreso_dinero'),
]