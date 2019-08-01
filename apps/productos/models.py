from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField()
    fabricante = models.CharField(max_length=10)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=6)
    porc_descuento = models.FloatField()
    iva = models.FloatField()
    unidades = models.IntegerField()
    activo = models.BooleanField(default = True)


def media_directory_path(instance, filename):
    model_name = instance.__class__.__name__
    return os.path.join(model_name, filename)