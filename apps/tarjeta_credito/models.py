from django.db import models

# Create your models here.
class Tarjeta_credito(models.Model):
    numero_tarjeta = models.CharField(max_length=16, primary_key=True)
    
    #Entidades de tarjetas
    AMERICAN_EXPRESS = 'American Express'
    VISA = 'Visa'
    MASTER_CARD = 'Master Card'

    ENTIDAD_TARJETA_CHOICES={
        (AMERICAN_EXPRESS, 'american_express'),
        (VISA, 'visa'),
        (MASTER_CARD, 'master_card'),
    }

    entidad = models.CharField(
        choices=ENTIDAD_TARJETA_CHOICES,
        max_length=20,
        default=MASTER_CARD
    )

    factura = models.ManyToManyField('facturas.Factura', through='pagos_credito.Pago_credito')

    titular = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)