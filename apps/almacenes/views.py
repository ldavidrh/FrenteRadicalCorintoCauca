from django.shortcuts import render, redirect
from .forms import FormularioCreacionAlmacen
from django.contrib import messages
from .models import Almacen
from apps.inventario.models import Inventario
from apps.categorias.models import Categoria
from apps.productos.models import Producto

# Create your views here.
def crear_almacen_view(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = FormularioCreacionAlmacen(request.POST)
        if form.is_valid():
            almacen = form.save()
            productos = Producto.objects.all()
            for producto in productos:
                inventario = Inventario()
                inventario.almacen = almacen
                inventario.producto = producto
                inventario.cantidad = 1
                inventario.save()
            messages.success(request, 'Almacen registrado existosamente')
            redirect('almacenes:crear_almacen')
    else:
        form = FormularioCreacionAlmacen()

    return render(request, 'almacenes/registro.html', {'form': form, 'categorias': categorias})

def consultar_almacenes_view(request):
    categorias = Categoria.objects.all()
    almacenes = Almacen.objects.all()
    return render(request, 'almacenes/consultar.html', {'almacenes': almacenes, 'categorias': categorias})


def modificar_almacen_view(request, id):
    categorias = Categoria.objects.all()
    almacen = Almacen.objects.get(id=id)
    if request.method == 'GET':
        form = FormularioCreacionAlmacen(instance = almacen)
    else:
        form = FormularioCreacionAlmacen(request.POST, instance = almacen)
        if form.is_valid():
            form.save()
            messages.success(request, 'Almacen modificado exitosamente')
        return redirect('almacenes:consultar_almacenes')

    return render(request, 'almacenes/modificar.html', {'form': form, 'categorias': categorias})

def eliminar_almacen_view(request, id):
    almacen = Almacen.objects.filter(pk = id).delete()
    messages.success(request, 'Almacen eliminado exitosamente')
    return redirect('almacenes:consultar_almacenes')
