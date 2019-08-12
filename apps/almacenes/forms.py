from django import forms
from .models import Almacen

class FormularioCreacionAlmacen(forms.ModelForm):
    class Meta():
        model = Almacen
        fields = ('codigo', 'ciudad', 'direccion', 'producto')