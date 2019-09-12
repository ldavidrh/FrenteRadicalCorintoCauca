from django import forms
from .models import Producto, Detalle

class FormularioRegistroProducto(forms.ModelForm):
    class Meta():
        model = Producto
        fields = ('codigo', 'nombre', 'fabricante', 'descripcion', 'precio', 'subcategoria', 'imagen')

class FormularioRegistroDetail(forms.ModelForm):
    class Meta():
        model = Detalle
        fields = ('detalle',)

class FormularioModificarProducto(forms.ModelForm):
    class Meta():
        model = Producto
        fields = ('nombre', 'fabricante', 'descripcion', 'precio', 'subcategoria', 'imagen')