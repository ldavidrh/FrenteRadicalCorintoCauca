from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    precio = models.FloatField()