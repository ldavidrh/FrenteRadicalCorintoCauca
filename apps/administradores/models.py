from django.db import models
from usuarios import Usuario

# Create your models here.
class Administrador():
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)