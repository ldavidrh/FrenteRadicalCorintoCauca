from django.db import models

# Create your models here.
class Carrito(models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)