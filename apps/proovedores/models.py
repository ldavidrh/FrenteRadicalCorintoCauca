from django.db import models

# Create your models here.
class Proovedor(models.Model):
    nit = models.IntegerField(primary_key = True)
    direccion = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 10)
    activo = models.BooleanField(default = True)