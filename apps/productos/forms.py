from django import forms
from .models import Producto

class FormularioRegistroProducto():
    class Meta():
        model = Producto
       # field() 