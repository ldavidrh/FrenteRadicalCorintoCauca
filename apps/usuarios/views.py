from django.shortcuts import render, redirect
from .forms import FormularioRegistroGerente
from .forms import FormularioModificarGerente
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

# Create your views here.
def registroGerente_view(request):
    if request.method == 'POST':
        form = FormularioRegistroGerente(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            email = form.cleaned_data.get('email')
            instance.username = email
            instance.is_staff = 't'
            instance.save()
            messages.success(request, 'Gerente registrado exitosamente')
            return redirect('gerentes:registro')
    else:
        form = FormularioRegistroGerente()

    return render(request, 'gerentes/crearGerente.html', {'form':form})

def consultarGerentes_view(request):
    gerentes = Usuario.objects.filter(is_staff='t', is_superuser='f')
    return render(request, 'gerentes/consultar.html', {'gerentes': gerentes})

def eliminarGerente_view(request, numero_documento):
    gerente = Usuario.objects.get(numero_documento=numero_documento)
    if request.method == 'GET':
        gerente.is_active = 'f'
        gerente.save()
        messages.success(request, 'Gerente eliminado exitosamente')
        return redirect('gerentes:consulta')

def activarGerente_view(request, numero_documento):
    gerente = Usuario.objects.get(numero_documento=numero_documento)
    if request.method == 'GET':
        gerente.is_active = 't'
        gerente.save()
        messages.success(request, 'Gerente recontratado exitosamente')
        return redirect('gerentes:consulta')


def modificarGerente_view(request, numero_documento):
    gerente = Usuario.objects.get(numero_documento=numero_documento)
    if request.method == 'GET':
        form = FormularioModificarGerente(instance = gerente)
    else:
        form = FormularioModificarGerente(request.POST, instance = gerente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gerente modificado exitosamente')
        return redirect('gerentes:consulta')

    return render(request, 'gerentes/modificar.html', {'form': form})