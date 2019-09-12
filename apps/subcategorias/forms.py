from django import forms
from .models import Subcategoria
from apps.categorias.models import Categoria

class FormularioCreacionSubcategoria(forms.ModelForm):
    class Meta():
        model = Subcategoria
        fields = ('nombre', 'categoria')
