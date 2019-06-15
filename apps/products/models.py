from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 30)
    description = models.TextField()
    price = models.IntegerField(default=0)
    active = models.BooleanField(default = True)