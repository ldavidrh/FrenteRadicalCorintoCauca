from django.urls import path
from apps.facturas.views import *

app_name = 'facturas'

urlpatterns = [
    path('pago/<str:ciudad>', pago_view, name='pago'),
]