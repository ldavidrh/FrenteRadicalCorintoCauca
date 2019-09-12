from django.db import models

# Create your models here.
class Subcategoria(models.Model):
    nombre = models.CharField(max_length=30)

    categoria = models.ForeignKey('categorias.Categoria', on_delete=models.CASCADE, null = False, related_name = 'subcategorias')

    def __str__(self):
        return self.nombre