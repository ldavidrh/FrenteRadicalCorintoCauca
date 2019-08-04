from django.db import models
from django.conf import settings

# Create your models here.
class Cliente(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telefono = models.CharField(max_length = 10)
    direccion = models.CharField(max_length = 40)
