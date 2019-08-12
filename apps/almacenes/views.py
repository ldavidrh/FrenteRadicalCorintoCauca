from django.shortcuts import render, redirect
from .forms import FormularioCreacionAlmacen
from django.contrib import messages
from .models import Almacen

# Create your views here.
def crear_almacen_view(request):
    if request.method == 'POST':
        form = FormularioCreacionAlmacen(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Almacen registrado existosamente')
            redirect('almacenes:crear_almacen')
    else:
        form = FormularioCreacionAlmacen()

    return render(request, 'almacenes/registro.html', {'form': form})

def consultar_almacenes_view(request):
    almacenes = Almacen.objects.all().values()
    return render(request, 'almacenes/consultar.html', {'almacenes': almacenes})


def modificar_almacen_view(request, id):
    almacen = Almacen.objects.get(codigo = id)
    if request.method == 'GET':
        form = FormularioCreacionAlmacen(instance = almacen)
    else:
        form = FormularioCreacionAlmacen(request.POST, instance = almacen)
        if form.is_valid():
            form.save()
            messages.success(request, 'Almacen modificado exitosamente')
        return redirect('almacenes:consultar_almacenes')

    return render(request, 'almacenes/modificar.html', {'form': form})

