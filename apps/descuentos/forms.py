from django import forms
from .models import Descuento
from datetime import datetime
from bootstrap_datepicker_plus import DatePickerInput
        
class FormularioCreacionDescuento(forms.ModelForm):
    def clean(self):
        cleaned_data = super(FormularioCreacionDescuento, self).clean()
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_fin:
            fecha_fin = ('%s' % (fecha_fin))
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
            if datetime.today() >= fecha_fin:
                msg = u"Por favor ingrese una fecha valida para el descuento"
                self.add_error('fecha_fin', msg)      
                
        return cleaned_data
    class Meta():
        model = Descuento
        fields = ('id', 'porcentaje', 'fecha_fin', 'producto')
        widgets = {
            'fecha_fin': forms.DateTimeInput(attrs={'class':'datetime-input'}),
        }