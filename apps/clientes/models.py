from django.db import models
from apps.usuarios.models import Usuario
from django.conf import settings

# Create your models here.
class Cliente(Usuario):
    
    telefono = models.CharField(max_length = 10)
    direccion = models.CharField(max_length = 40)
