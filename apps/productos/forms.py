from django import forms
from .models import Producto

class FormularioRegistroProducto(forms.ModelForm):
    class Meta():
        model = Producto
        fields = ('codigo', 'nombre', 'fabricante', 'descripcion', 'precio', 'subcategoria', 'imagen')

class FormularioModificarProducto(forms.ModelForm):
    class Meta():
        model = Producto
        fields = ('nombre', 'fabricante', 'descripcion', 'precio', 'subcategoria', 'imagen')