from django.db import models

# Create your models here.


class Almacen(models.Model):
    # Ciudades
    CALI = 'Cali'
    BOGOTA = 'Bogota'
    MEDELLIN = 'Medellin'
    BARRANQUILLA = 'Barranquilla'
    CARTAGENA = 'Cartagena'
    CUCUTA = 'Cucuta'
    IBAGUE = 'Ibague'
    PASTO = 'Pasto'

    CIUDAD_CHOICES = {
        (CALI, 'Cali'),
        (BOGOTA, 'Bogota'),
        (MEDELLIN, 'Medellin'),
        (BARRANQUILLA, 'Barranquilla'),
        (CARTAGENA, 'Cartagena'),
        (CUCUTA, 'Cucuta'),
        (IBAGUE, 'Ibague'),
        (PASTO, 'Pasto'),
    }

    ciudad = models.CharField(
        choices=CIUDAD_CHOICES,
        max_length=20,
        default=CALI,
        unique=True
    )

    direccion = models.CharField(max_length=30)

    producto = models.ManyToManyField(
        'productos.Producto', blank=True, through='inventario.Inventario')

    def __str__(self):
        return self.ciudad
