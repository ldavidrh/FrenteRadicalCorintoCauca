from django.urls import path
from apps.clientes.views import *

app_name = 'clientes'
urlpatterns=[
    path('registro/', registro_view, name = 'registro'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
]
