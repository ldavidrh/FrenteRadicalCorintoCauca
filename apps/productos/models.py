from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    imagen = models.TextField()
    fabricante = models.TextField()
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places = 2, max_digits = 6)
    porc_descuento = models.FloatField()
    iva = models.FloatField()
    unidades = models.IntegerField()
    detalles = models.TextField()
    activo = models.BooleanField(default = True)