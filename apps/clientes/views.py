from django.shortcuts import render, redirect
from .forms import FormularioRegistroCliente
from django.contrib import messages


# Create your views here.
def registro(request):
    if request.method == 'POST':
        forms = FormularioRegistroCliente(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            numero_documento = form.cleaned_data.get('numero_documento')
            instance.username = numero_documento
            instance.save()
            messsages.success(request, 'Cliente registrado exitosamente')
            return redirect('inicio')
        
    else:
        forms = FormularioRegistroCliente()
    
    return render(request, 'clientes/registro.html', {'form':forms})