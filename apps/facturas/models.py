from django.db import models

# Create your models here.
class Factura(models.Model):
    numero = models.CharField(max_length = 30, primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    subtotal = models.DecimalField(decimal_places = 2, max_digits = 7)
    total_iva = models.DecimalField(decimal_places = 2, max_digits = 7)
    total = models.DecimalField(decimal_places = 2, max_digits = 7)

    cliente = models.ForeignKey('usurios.Usuario', on_delete = models.CASCADE)

    producto = models.ManyToManyField('productos.Producto', through='productos_vendidos.Producto_vendido')
