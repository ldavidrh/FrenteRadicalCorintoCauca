from django.db import models

# Create your models here.
class Tarjeta_debito(models.Model):
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

    #Tipo de cuentas de tarjeta de debito
    CUENTA_AHORROS = 'Cuenta de ahorros'
    CUENTA_CORRIENTE = 'Cuenta corriente'

    TIPO_CUENTA_CHOICES = {
        (CUENTA_AHORROS, 'cuenta_ahorros'),
        (CUENTA_CORRIENTE, 'cuenta_corriente'),
    }

    tipo_cuenta = models.CharField(
        choices=TIPO_CUENTA_CHOICES,
        max_length=20,
        default=CUENTA_AHORROS
    )

    factura = models.ManyToManyField('facturas.Factura', through='pagos_debito.Pago_debito')

    titular = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)

