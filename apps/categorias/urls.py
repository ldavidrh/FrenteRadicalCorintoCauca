from django.urls import path
from apps.categorias.views import *

app_name = 'categorias'

urlpatterns=[
    path('crear_categoria/', crear_categoria_view, name = 'crear_categoria'),
    path('consultar_categoria/', consultar_categorias_view, name = 'consultar_categorias'),
    path('eliminar_categoria/<int:id>', eliminar_categoria_view, name = 'eliminar_categoria'),
    #path('editar_categoria/<int:id>', editar_categoria_view, name = 'editar_categoria'),
]