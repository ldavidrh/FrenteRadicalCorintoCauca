from django.shortcuts import render, redirect
from .forms import FormularioAdicionInventario
from django.contrib import messages
#from .models import Categoria

# Create your views here.
def agregar_view(request):
    if request.method == 'POST':
        form = FormularioAdicionInventario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado a almacen exitosamente')
            return redirect('inventario:agregar')
    else:
        form = FormularioAdicionInventario()

    return render(request, 'inventario/agregar.html', {'form':form})
        