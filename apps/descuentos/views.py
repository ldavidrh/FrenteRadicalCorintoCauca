from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioCreacionDescuento
from .models import Descuento
from apps.productos.models import Producto
from apps.categorias.models import Categoria

# Create your views here.
def registrar_view(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = FormularioCreacionDescuento(request.POST)
        if form.is_valid():
            form.save(commit = False)
            id = form.cleaned_data['producto'].codigo
            descuento_exist = (Descuento.objects.filter(producto = id).count() > 0)
            if descuento_exist:
                messages.warning(request, 'El producto ya tiene un descuento, puede modificarlo en la pestaña de consultar descuentos')
                return redirect('descuentos:registrar')
            else:
                form.save()
                porcentaje = (form.cleaned_data['porcentaje'])
                producto = Producto.objects.get(codigo = id)
                oferta = producto.precio - (producto.precio * porcentaje)/100
                producto.oferta = oferta
                producto.save()
                messages.success(request, 'Descuento registrado exitosamente')
                return redirect('descuentos:registrar')
    else:
        form = FormularioCreacionDescuento()

    return render(request, 'descuentos/registro.html', {'form': form, 'categorias': categorias})


def consultar_view(request):
    descuentos = Descuento.objects.all().values()
    categorias = Categoria.objects.all()
    return render(request, 'descuentos/consultar.html', {'descuentos': descuentos, 'categorias': categorias})


def modificar_view(request, id):
    categorias = Categoria.objects.all()
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
