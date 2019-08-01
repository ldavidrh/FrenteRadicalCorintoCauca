from django.db import model
from usuarios import Usuario

# Create your models here.
class Clientes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    correo = models.EmailField(max_length=40)
    telefono = models.CharField(max_length = 10)
    direccion = models.CharField(max_length = 40)
