from django.urls import path
from .views import *

app_name = 'descuentos'

urlpatterns = [
    path('registrar/', registrar_view, name = 'registrar'),
    path('consultar/', consultar_view, name = 'consultar'),
    path('modificar/<int:id>', modificar_view, name = 'modificar'),
    path('eliminar/<int:id>', eliminar_view, name = 'eliminar'),
]