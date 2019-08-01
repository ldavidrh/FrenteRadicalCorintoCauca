from django.db import models

# Create your models here.
class Subcategoria(models.Model):
    codigo = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=30)

    categoria = models.ForeignKey('categorias.Categoria', on_delete=models.CASCADE)