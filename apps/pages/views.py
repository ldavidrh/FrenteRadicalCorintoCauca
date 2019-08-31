from django.shortcuts import render, redirect
from apps.categorias.models import Categoria
from apps.productos.models import Producto
from apps.carritos.models import Carrito
from apps.almacenes.forms import FormularioCiudad
from apps.descuentos.models import Descuento
from apps.descuentos.views import *
from datetime import datetime
from django.db.models import Q

# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    if not request.user.is_authenticated:
        carritos = None
    else:
        cliente = request.user
        carritos = Carrito.objects.filter(cliente = cliente)
    form_ciudades = FormularioCiudad()

    descuentos = Descuento.objects.all()

    for descuento in descuentos:
    
        fecha_fin = descuento.fecha_fin

        if fecha_fin:
            fecha_fin = ('%s' % (fecha_fin))
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
            if datetime.today() >= fecha_fin:
                producto = descuento.producto
                producto.oferta = producto.precio
                producto.save()
                descuento.delete()
    
    queryset = request.GET.get("buscar")
    
    if queryset:
        productos = Producto.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(descripcion__icontains = queryset) |
            Q(subcategoria__nombre__icontains = queryset) |
            Q(subcategoria__categoria__nombre__icontains = queryset)
        ).distinct()

    return render(request, 'home.html', {'productos':productos, 'categorias': categorias, 'form_ciudades': form_ciudades, 'carritos':carritos})


