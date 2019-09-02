from django import forms
from .models import Carrito

class FormularioCarrito(forms.ModelForm):
    class Meta():
        model = Carrito
        fields = ('cantidad',)