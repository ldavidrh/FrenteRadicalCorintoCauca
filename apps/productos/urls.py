from django.urls import path
from .views import *

app_name = 'productos'

urlpatterns=[
    path('registrar/', registrar_view, name = 'registrar')
]