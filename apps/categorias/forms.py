from django import forms
from .models import Categoria

class FormularioCreacionCategoria(forms.ModelForm):
    class Meta():
        model = Categoria
        fields = ('nombre',)