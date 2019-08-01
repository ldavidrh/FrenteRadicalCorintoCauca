from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)

    #Tipo de documento
    TARJETA_IDENTIDAD = 'Tarjeta de identidad'
    CEDULA = 'Cedula de ciudadania'
    PASAPORTE = 'Pasaporte'
    TIPO_DOCUMENTO_CHOICES={
        (TARJETA_IDENTIDAD, 'tarjeta_identidad'),
        (CEDULA, 'cedula'),
        (PASAPORTE, 'pasaporte'),
    }

    tipo_documento = models.CharField(
        max_length = 30,
        choices = TIPO_DOCUMENTO_CHOICES,
        default = CEDULA
    )
    numero_documento = models.CharField(max_length = 30, primary_key = True)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default = True)