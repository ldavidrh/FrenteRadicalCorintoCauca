from django.shortcuts import render, redirect
from .models import Carrito
from apps.productos.models import Producto
from apps.usuarios.models import Usuario
from apps.categorias.models import Categoria
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def addToCart_view(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    cliente = request.user
    producto_exist = (Carrito.objects.filter(cliente = cliente, producto = producto).count() > 0)
    if producto_exist:
        messages.warning(request, 'El producto ya se encuentra en el carrito')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        carrito = Carrito()
        carrito.cantidad = 1
        carrito.producto = producto
        carrito.cliente = cliente
        carrito.save()
        messages.success(request, 'Producto añadido exitosamente')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def consultarCarrito_view(request):
    categorias = Categoria.objects.all()

    if not request.user.is_authenticated:
        carritos = None
    else:
        cliente = request.user
        carritos = Carrito.objects.filter(cliente = cliente)

    return render(request, 'carrito/carrito.html', {'categorias': categorias, 'carritos':carritos})
    

    
