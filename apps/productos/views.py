from django.shortcuts import render, redirect
from .forms import FormularioRegistroProducto
from django.contrib import messages

# Create your views here.
def registrar_view(request):
    if request.method == 'POST':
        form = FormularioRegistroProducto(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto registrado exitosamente')
            return redirect('productos:registrar')
    else:
        form = FormularioRegistroProducto()

    return render(request, 'productos/registro.html', {'form': form})
