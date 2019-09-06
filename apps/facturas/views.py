from django.shortcuts import render, redirect
from apps.carritos.models import Carrito
from .forms  import FormularioPagoCredito, FormularioPagoDebito
from apps.almacenes.forms import FormularioCiudad
from apps.productos.models import Producto
from apps.usuarios.models import Usuario
from apps.almacenes.models import Almacen
from apps.categorias.models import Categoria
from apps.inventario.models import Inventario
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from apps.almacenes.models import Almacen
from apps.productos_vendidos.models import Producto_vendido
from .models import Factura, Pago_credito, Pago_debito
from decimal import Decimal
# Create your views here.

def pago_view(request, ciudad):
    categorias = Categoria.objects.all()
    #CARRITO
    if not request.user.is_authenticated:
        carritos = None
    else:
        cliente = request.user
        carritos = Carrito.objects.filter(cliente = cliente)

    subtotal = 0.00
    totalIva = 0.00
    total = 0.00

    for carrito in carritos:
        subtotal = subtotal + float((carrito.producto.oferta * carrito.cantidad))

    totalIva = (subtotal * 0.19)
    total = subtotal + totalIva

    if request.method == 'POST':
        formC = FormularioPagoCredito(request.POST)
        formD = FormularioPagoDebito(request.POST)
        if 'e' in request.POST:
            #CREANDO FACTURA
            factura = Factura()
            factura.subtotal = Decimal(subtotal)
            factura.total_iva = Decimal(totalIva)
            factura.total = Decimal(total)
            factura.almacen = Almacen.objects.get(ciudad = ciudad)
            factura.cliente = request.user
            factura.save()
            for carrito in carritos:
                #COMPRANDO LOS PRODUCTOS
                producto_vendido = Producto_vendido()
                producto_vendido.factura =  factura
                producto_vendido.producto = carrito.producto
                producto_vendido.precio = carrito.producto.precio
                producto_vendido.oferta = carrito.producto.oferta
                producto_vendido.cantidad_vendida = carrito.cantidad
                producto_vendido.save()
                #ELIMINANDO LOS PRODUCTOS DEL INVENTARIO
                inventario = Inventario.objects.get(almacen = Almacen.objects.get(ciudad = ciudad), producto = carrito.producto)
                inventario.cantidad =  inventario.cantidad - carrito.cantidad
                inventario.save()
                #ELIMINANDO LOS PRODUCTOS DEL CARRITO
                carrito.delete()
            
            messages.success(request, 'Compra finalizada exitosamente')
            return redirect('home')
        else:
            if 'c' in request.POST:
                form = formC
            elif 'd' in request.POST:
                form = formD
            if form.is_valid():
                #CREANDO FACTURA
                factura = Factura()
                factura.subtotal = Decimal(subtotal)
                factura.total_iva = Decimal(totalIva)
                factura.total = Decimal(total)
                factura.almacen = Almacen.objects.get(ciudad = ciudad)
                factura.cliente = request.user
                factura.save()
                for carrito in carritos:
                    #COMPRANDO LOS PRODUCTOS
                    producto_vendido = Producto_vendido()
                    producto_vendido.factura =  factura
                    producto_vendido.producto = carrito.producto
                    producto_vendido.precio = carrito.producto.precio
                    producto_vendido.oferta = carrito.producto.oferta
                    producto_vendido.cantidad_vendida = carrito.cantidad
                    producto_vendido.save()
                    #ELIMINANDO LOS PRODUCTOS DEL INVENTARIO
                    inventario = Inventario.objects.get(almacen = Almacen.objects.get(ciudad = ciudad), producto = carrito.producto)
                    inventario.cantidad =  inventario.cantidad - carrito.cantidad
                    inventario.save()
                    #ELIMINANDO LOS PRODUCTOS DEL CARRITO
                    carrito.delete()

                #CREANDO METODO DE PAGO
                pago = form.save(commit = False)
                pago.factura = factura
                pago.total = total
                pago.save()
                messages.success(request, 'Compra finalizada exitosamente')
                return redirect('home')
    else:
        formC = FormularioPagoCredito()
        formD = FormularioPagoDebito()

    
    #BARRA BUSQUEDA
    queryset = request.GET.get("buscar")

    if queryset:
        productos = Producto.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(descripcion__icontains = queryset)|
            Q(subcategoria__nombre__icontains = queryset) |
            Q(subcategoria__categoria__nombre__icontains = queryset)
        ).distinct()
        return render(request, 'home.html', {'productos':productos, 'categorias': categorias, 'carritos':carritos})
    else:
        return render(request, 'ventas/realizarCompra.html', {'formC': formC, 'formD': formD, 'categorias': categorias, 'carritos':carritos, 'ciudad': ciudad})