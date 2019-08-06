from django.shortcuts import render, redirect
from .forms import FormularioRegistroCliente
from django.contrib import messages


# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = FormularioRegistroCliente(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            numero_documento = form.cleaned_data.get('numero_documento')
            instance.username = form.cleaned_data.get('email')
            instance.save()
            messages.success(request, 'Cliente registrado exitosamente')
            return redirect('home')
        
    else:
        form = FormularioRegistroCliente()

    return render(request, 'clientes/registro.html', {'form':form})