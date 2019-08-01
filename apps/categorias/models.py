from django.db import models

# Create your models here.
class Categoria(models.Model):
    codigo = models.CharFields(max_length = 10, primary_key = True)
    nombre = models.CharFields(max_length = 30)
