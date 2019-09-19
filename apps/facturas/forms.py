from django import forms
from .models import Factura, Pago_credito, Pago_debito

class FormularioPagoDebito(forms.ModelForm):
    class Meta():
        model = Pago_debito
        fields = ('numero_tarjeta', 'entidad', 'tipo_cuenta')

class FormularioPagoCredito(forms.ModelForm):
    class Meta():
        model = Pago_credito
        fields = ('numero_tarjeta', 'entidad', 'cuotas')