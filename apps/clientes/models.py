from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.TextField()
    tipo_documento = models.TextField()
    num_documento = models.IntegerField(primary_key=True)
    telefono = models.IntegerField()
    direccion = models.TextField()
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default = True)