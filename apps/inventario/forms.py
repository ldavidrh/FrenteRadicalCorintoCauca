from django import forms
from .models import Inventario
class FormularioAdicionInventario(forms.ModelForm):
    class Meta():
        model = Inventario
        fields = ('almacen', 'producto', 'cantidad')