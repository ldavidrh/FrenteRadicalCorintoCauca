from django.db import models

# Create your models here.
class Descuento(models.Model):
    porcentaje = models.IntegerField()
    fecha_inicio = models.DateField(auto_now_add = True)
    fecha_fin = models.DateField(null = False)

    producto = models.ForeignKey(
        'productos.Producto', on_delete=models.CASCADE, null = False, related_name = 'descuentos'
    )