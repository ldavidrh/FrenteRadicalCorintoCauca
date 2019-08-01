from django.db import models
from productos import Producto
# Create your models here.
class Detalle(models.Model):
    codigo = models.CharField(max_length=7, primary_key=True)
    descripcion = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=CASCADE)