from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm

class FormularioRegistroCliente(UserCreationForm):
    class Meta():
        model = Cliente
        fields = ('first_name', 'last_name', 'tipo_documento', 'numero_documento', 'fecha_nacimiento', 'email','direccion', 'telefono', 'password1', 'password2')
        