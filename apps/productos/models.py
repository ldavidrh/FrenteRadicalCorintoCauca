from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos')
    fabricante = models.CharField(max_length=10)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    iva = models.FloatField(default=19.0)
    oferta = models.DecimalField(decimal_places=2, max_digits=10, default = 0.00)

    subcategoria = models.ForeignKey(
        'subcategorias.Subcategoria', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class Detalle(models.Model):
    detalle = models.CharField(max_length=100)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)


def media_directory_path(instance, filename):
    model_name = instance.__class__.__name__
    return os.path.join(model_name, filename)
