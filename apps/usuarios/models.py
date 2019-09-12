from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    class Meta:
        ordering = ['first_name', 'last_name']

        def __str__(self):
            return self.get_full_name()

    #Tipo de documento
    TARJETA_IDENTIDAD = 'Tarjeta de identidad'
    CEDULA = 'Cedula de ciudadania'
    PASAPORTE = 'Pasaporte'
    TIPO_DOCUMENTO_CHOICES={
        (TARJETA_IDENTIDAD, 'Tarjeta de identidad'),
        (CEDULA, 'Cedula de ciudadania'),
        (PASAPORTE, 'Pasaporte'),
    }

    tipo_documento = models.CharField(
        max_length = 30,
        choices = TIPO_DOCUMENTO_CHOICES,
        default = CEDULA
    )
    numero_documento = models.CharField(max_length = 30, primary_key = True)
    fecha_nacimiento = models.DateField()
    