from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioCreacionDescuento

# Create your views here.
def registrar_view(request):
    if request.method == 'POST':
        form = FormularioCreacionDescuento(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Descuento registrado exitosamente')
            return redirect('descuentos:registrar')
    else:
        form = FormularioCreacionDescuento()

    return render(request, 'descuentos/registro.html', {'form': form})