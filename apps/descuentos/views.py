from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioCreacionDescuento
from .models import Descuento
from apps.categorias.models import Categoria

# Create your views here.
def registrar_view(request):
    categorias = Categoria.objects.all().values()
    if request.method == 'POST':
        form = FormularioCreacionDescuento(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Descuento registrado exitosamente')
            return redirect('descuentos:registrar')
    else:
        form = FormularioCreacionDescuento()

    return render(request, 'descuentos/registro.html', {'form': form, 'categorias': categorias})


def consultar_view(request):
    descuentos = Descuento.objects.all().values()
    categorias = Categoria.objects.all().values()
    return render(request, 'descuentos/consultar.html', {'descuentos': descuentos, 'categorias': categorias})


def modificar_view(request, id):
    categorias = Categoria.objects.all().values()
    descuento = Descuento.objects.get(pk = id)
    if request.method == 'GET':
        form = FormularioCreacionDescuento(instance = descuento)
    else:
        form = FormularioCreacionDescuento(request.POST, instance = descuento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Descuento modificado exitosamente')
        return redirect('descuentos:consultar')
    
    return render(request, 'descuentos/modificar.html', {'form':form, 'categorias':categorias})

def eliminar_view(request, id):
    descuento = Descuento.objects.filter(pk=id).delete()
    return redirect('descuentos:consultar')