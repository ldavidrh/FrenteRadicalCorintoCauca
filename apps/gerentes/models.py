from django.db import models
from usuarios import Usuario

# Create your models here.
class Gerente(models.Model):
    usuario = models.ForeingKey(Usuario, on_delete=models.CASCADE)