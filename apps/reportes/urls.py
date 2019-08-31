from django.urls import path
from .views import *
app_name='reportes'

urlpatterns= [
    path('test/', get_data, name = 'test'),
]