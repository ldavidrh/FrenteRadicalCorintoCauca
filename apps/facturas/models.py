from django.db import models

# Create your models here.
class Factura(models.Model):
    fecha = models.DateField(auto_now_add = True)
    hora = models.TimeField(auto_now_add = True)
    subtotal = models.DecimalField(decimal_places = 2, max_digits = 14)
    total_iva = models.DecimalField(decimal_places = 2, max_digits = 14)
    total = models.DecimalField(decimal_places = 2, max_digits = 14)

    almacen = models.ForeignKey('almacenes.Almacen', on_delete = models.CASCADE)

    cliente = models.ForeignKey('usuarios.Usuario', on_delete = models.CASCADE)

    producto = models.ManyToManyField('productos.Producto', through='productos_vendidos.Producto_vendido')

class Pago_debito(models.Model):
    #Tipo de cuentas de tarjeta de debito

    TIPO_CUENTA_CHOICES = {
        ('Cuenta de ahorros', 'Cuenta de ahorros'),
        ('Cuenta de corriente', 'Cuenta corriente'),
    }

    tipo_cuenta = models.CharField(
        choices=TIPO_CUENTA_CHOICES,
        max_length=20,
        blank=True
    )
    #ENTIDADES
    ENTIDAD_TARJETA_CHOICES={
        ('american_express', 'AMERICAN EXPRESS'),
        ('visa', 'VISA'),
        ('master_card', 'MASTER CARD'),
    }

    entidad = models.CharField(
        choices=ENTIDAD_TARJETA_CHOICES,
        max_length=20,
        blank=True
    )
    
    numero_tarjeta = models.CharField(max_length=16)
    numero_aprobacion = models.CharField(max_length=10)
    fecha_aprobacion = models.DateField()
    hora_aprobacion = models.TimeField()
    total = models.DecimalField(decimal_places = 2, max_digits = 14, null=True)

    factura = models.ForeignKey('facturas.Factura', on_delete=models.CASCADE, null=True, related_name = 'debito')

class Pago_credito(models.Model):
    #Cuotas
    CUOTAS = [tuple([x,x]) for x in range (1, 37)]

    cuotas = models.IntegerField(
        choices=CUOTAS,
        blank=True
    )
    #ENTIDADES
    ENTIDAD_TARJETA_CHOICES={
        ('american_express', 'AMERICAN EXPRESS'),
        ('visa', 'VISA'),
        ('master_card', 'MASTER CARD'),
    }

    entidad = models.CharField(
        choices=ENTIDAD_TARJETA_CHOICES,
        max_length=20,
        blank=True
    )

    numero_tarjeta = models.CharField(max_length=16)
    numero_aprobacion = models.CharField(max_length=10)
    fecha_aprobacion = models.DateField()
    hora_aprobacion = models.TimeField()
    total = models.DecimalField(decimal_places = 2, max_digits = 14, null=True)

    factura = models.ForeignKey('facturas.Factura', on_delete=models.CASCADE, null=True, related_name = 'credito')