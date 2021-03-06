from django import forms
from .models import Cliente
from ..usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime



class FormularioRegistroCliente(UserCreationForm):
    def clean(self):
        cleaned_data = super(FormularioRegistroCliente, self).clean()
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')
        user_exists = (Usuario.objects.filter(username = cleaned_data.get('email')).count() > 0)

        if fecha_nacimiento:
            fecha_nacimiento = ('%s' % (fecha_nacimiento))
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
            if datetime.today() <= fecha_nacimiento:
                msg = u"Por favor ingrese una fecha de nacimiento valida"
                self.add_error('fecha_nacimiento', msg)
                
        if user_exists:
            msg = u"Ya existe un usuario registrado con este correo electronico"
            self.add_error('email', msg)        
                
        return cleaned_data

    class Meta():
        model = Cliente
        fields = ('first_name', 'last_name', 'tipo_documento', 'numero_documento', 'fecha_nacimiento', 'telefono','direccion', 'email', 'password1', 'password2')


class FormularioModificarCliente(forms.ModelForm):
    def clean(self):
        cleaned_data = super(FormularioModificarCliente, self).clean()
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')
        
        if fecha_nacimiento:
            fecha_nacimiento = ('%s' % (fecha_nacimiento))
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
            if datetime.today() <= fecha_nacimiento:
                msg = u"Por favor ingrese una fecha de nacimiento valida"
                self.add_error('fecha_nacimiento', msg)       
                        
        return cleaned_data
    
    class Meta():
        model = Cliente
        fields = ('first_name', 'last_name', 'fecha_nacimiento', 'telefono','direccion')

class FormularioModificarCuenta(forms.ModelForm):
    def clean(self):
        cleaned_data = super(FormularioModificarCuenta, self).clean()
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')
                
        if fecha_nacimiento:
            fecha_nacimiento = ('%s' % (fecha_nacimiento))
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
            if datetime.today() <= fecha_nacimiento:
                msg = u"Por favor ingrese una fecha de nacimiento valida"
                self.add_error('fecha_nacimiento', msg)       
                                
        return cleaned_data
            
    class Meta():
        model = Usuario
        fields = ('first_name', 'last_name', 'fecha_nacimiento')