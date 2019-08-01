from django.db import models

# Create your models here.
class Categoria(models.Model):
    codigo = models.CharField(max_length = 10, primary_key = True)
    nombre = models.CharField(max_length = 30)
