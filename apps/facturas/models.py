from django.db import models

# Create your models here.
class Factura(models.Model):
    codigo_factura = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    subtotal = models.DecimalField(decimal_places = 2, max_digits = 7)
    total_iva = models.DecimalField(decimal_places = 2, max_digits = 7)
    total = models.DecimalField(decimal_places = 2, max_digits = 7)
