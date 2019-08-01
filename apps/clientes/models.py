from django.db import models

# Create your models here.
class Cliente(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    correo = models.EmailField(max_length=40)
    telefono = models.CharField(max_length = 10)
    direccion = models.CharField(max_length = 40)
