from django.db import models

# Create your models here.
class Pago_debito(models.Model):
    numero_aprobacion = models.CharField(max_length=10, primary_key=True)
    fecha_aprobacion = models.DateField()
    hora_aprobacion = models.TimeField()

    factura = models.ForeignKey('facturas.Factura', on_delete=models.CASCADE)
    tarjeta_debito = models.ForeignKey('tarjeta_debito.Tarjeta_debito', on_delete=models.CASCADE)
