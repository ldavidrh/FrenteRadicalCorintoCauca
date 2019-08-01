from django.db import models
from apps.Productos import Producto
# Create your models here.
class Almacen(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    
    #Ciudades
    CALI = 'Cali'
    BOGOTA = 'Bogota'
    MEDELLIN = 'Medellin'
    BARRANQUILLA = 'Barranquilla'
    CARTAGENA = 'Cartagena'
    CUCUTA = 'Cucuta'
    IBAGUE = 'Ibague'
    PASTO = 'Pasto'


    CIUDAD_CHOICES={
        (CALI, 'cali'),
        (BOGOTA, 'bogota'),
        (MEDELLIN, 'medellin'),
        (BARRANQUILLA, 'barranquilla'),
        (CARTAGENA, 'cartagena'),
        (CUCUTA, 'cucuta'),
        (IBAGUE, 'ibague'),
        (PASTO, 'pasto'),
    }

    ciudad = models.CharField(
        choices = CIUDAD_CHOICES,
        max_value= 20,
        default = CALI 
    )

    direccion = models.CharField(max_length=30)