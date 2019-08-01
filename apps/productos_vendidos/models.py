from django.db import models

# Create your models here.
class Producto_vendido(models.Model):
    factura = models.ForeignKey('facturas.Factura', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()