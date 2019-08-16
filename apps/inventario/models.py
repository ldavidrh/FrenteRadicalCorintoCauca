from django.db import models

# Create your models here.
class Inventario(models.Model):
    almacen = models.ForeignKey('almacenes.Almacen', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)