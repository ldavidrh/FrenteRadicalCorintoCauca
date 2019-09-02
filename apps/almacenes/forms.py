from django import forms
from .models import Almacen

class FormularioCreacionAlmacen(forms.ModelForm):
    class Meta():
        model = Almacen
        fields = ('ciudad', 'direccion')

class FormularioCiudad(forms.ModelForm):
    almacenes = Almacen.objects.all()
    CIUDAD_CHOICES = [tuple([almacen.ciudad,almacen.ciudad]) for almacen in almacenes]

    ciudad = forms.ChoiceField(label='Ciudad', choices=CIUDAD_CHOICES)
    class Meta():
        model = Almacen
        fields = ('ciudad',)
