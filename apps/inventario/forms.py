from django import forms
from .models import Inventario
class FormularioCantidad(forms.ModelForm):
    class Meta():
        model = Inventario
        fields = ('cantidad',)