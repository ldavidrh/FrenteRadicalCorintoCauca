from django.urls import path
from apps.clientes.views import *

app_name = 'clientes'
urlpatterns=[
    path('base/', base_view, name = 'registro'),
]