from django import forms
from .models import Almacen

class FormularioCreacionAlmacen(forms.ModelForm):
    class Meta():
        model = Almacen
        fields = ('ciudad', 'direccion')

class FormularioCiudad(forms.ModelForm):
    #ciudad = forms.ModelChoiceField(queryset = Almacen.objects.all())
    
    class Meta():
        model = Almacen
        fields = ('ciudad',)
