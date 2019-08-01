from django.db import models

# Create your models here.
class Administrador():
    usuario = models.ForeignKey('usuarios.Usuario', on_delete = models.CASCADE)