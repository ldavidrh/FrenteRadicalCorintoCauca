from django.db import models

# Create your models here.
class Gerente(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)