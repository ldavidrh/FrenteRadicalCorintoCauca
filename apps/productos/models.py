from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(null = True)
    fabricante = models.CharField(max_length=10)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    iva = models.FloatField()
    
    subcategoria = models.ForeignKey('subcategorias.Subcategoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

def media_directory_path(instance, filename):
    model_name = instance.__class__.__name__
    return os.path.join(model_name, filename)