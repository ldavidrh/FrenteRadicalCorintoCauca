from django import forms
from .models import Descuento

class FormularioCreacionDescuento(forms.ModelForm):
    class Meta():
        model = Descuento
        fields = ('id', 'porcentaje', 'fecha_fin', 'producto')
