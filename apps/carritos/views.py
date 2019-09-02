from django.shortcuts import render, redirect
from .models import Carrito
from .forms  import FormularioCarrito
from apps.almacenes.forms import FormularioCiudad
from apps.productos.models import Producto
from apps.usuarios.models import Usuario
from apps.almacenes.models import Almacen
from apps.categorias.models import Categoria
from apps.inventario.models import Inventario
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def addToCart_view(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    cliente = request.user
    producto_exist = (Carrito.objects.filter(cliente = cliente, producto = producto).count() > 0)
    if producto_exist:
        messages.warning(request, 'El producto ya se encuentra en el carrito')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        almacen = Almacen.objects.get(ciudad=ciudad)
        inventario = Inventario.objects.get(almacen=almacen, producto=producto)
        cantInventario = int(inventario.cantidad)
        if cantInventario == 0:
            messages.warning(request, 'No quedan unidades de este producto')
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
    form_ciudades = FormularioCiudad()

    #CARRITO
    if not request.user.is_authenticated:
        carritos = None
    else:
        cliente = request.user
        carritos = Carrito.objects.filter(cliente = cliente)

    #CAMBIAR CIUDAD
    global ciudad
    try: 
        if not ciudad:
            ciudad = 'Cali'
    except:       
        ciudad = 'Cali'
    if request.method == 'POST':
        form = FormularioCiudad(request.POST)
        almacen = form.data['ciudad']
        ciudad = almacen
        for carrito in carritos:
            producto = carrito.producto
            almacen = Almacen.objects.get(ciudad=ciudad)
            inventario = Inventario.objects.get(almacen=almacen, producto=producto)
            cantInventario = int(inventario.cantidad)
            if cantInventario == 0:
                carrito.delete()
            else:
                carrito.cantidad = 1
                carrito.save()
        messages.success(request, 'Usted cambio de locación, ahora se encuentra en ' + ciudad)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = FormularioCiudad()
    
    queryset = request.GET.get("buscar")

    #BARRA BUSQUEDA
    if queryset:
        productos = Producto.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(descripcion__icontains = queryset)|
            Q(subcategoria__nombre__icontains = queryset) |
            Q(subcategoria__categoria__nombre__icontains = queryset)
        ).distinct()
        return render(request, 'home.html', {'productos':productos, 'categorias': categorias, 'carritos':carritos})
    else:
        return render(request, 'carritos/carrito.html', {'categorias': categorias, 'carritos':carritos, 'form_ciudades': form_ciudades, 'ciudad': ciudad})

def eliminarCarrito_view(request, id):
    carrito = Carrito.objects.get(pk=id)
    carrito.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cambiarCantidad_view(request, id):
    cantidad = int(request.POST["cantidad"])
    carrito = Carrito.objects.get(id=id)
    producto = carrito.producto
    try: 
        almacen = Almacen.objects.get(ciudad=ciudad)
    except:       
        almacen = Almacen.objects.get(ciudad='Cali')
    inventario = Inventario.objects.get(almacen=almacen, producto=producto)
    cantInventario = int(inventario.cantidad)

    if cantidad > 0 and cantidad <= cantInventario:
        carrito.cantidad = cantidad
        carrito.save()
    else:
        messages.warning(request, 'Solo existen ' + str(cantInventario) + ' unidades de este producto, por favor proporcione una cantidad valida')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



    