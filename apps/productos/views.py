from django.shortcuts import render, redirect
from .forms import FormularioRegistroProducto, FormularioModificarProducto, FormularioRegistroDetail
from django.contrib import messages
from .models import Producto
from .models import Detalle
from apps.categorias.models import Categoria
from apps.subcategorias.models import Subcategoria
from django.forms import modelformset_factory
from apps.carritos.models import Carrito

# Create your views here.
def registrar_view(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = FormularioRegistroProducto(request.POST, request.FILES)
        detalle_form = FormularioRegistroDetail(request.POST)
        if form.is_valid() and detalle_form.is_valid():
            producto = form.save()
            detalle = detalle_form.save(False)

            detalle.producto=producto
            detalle.save()

            messages.success(request, 'Producto registrado exitosamente')
            return redirect('productos:registrar')
    else:
        form = FormularioRegistroProducto()
        detalle_form = FormularioRegistroDetail()

    return render(request, 'productos/registro.html', {'form': form,'detalle_form': detalle_form, 'categorias': categorias})

def consultarProdutos_view(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    if not request.user.is_authenticated:
        carritos = None
    else:
        cliente = request.user
        carritos = Carrito.objects.filter(cliente = cliente)
        
    return render(request, 'productos/consultar.html',{'productos':productos, 'categorias': categorias, 'carritos':carritos})

def consultarPorSubcategoria_view(request, subcategoria_id):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(subcategoria_id = subcategoria_id)

    if not request.user.is_authenticated:
        carritos = None
    else:
        cliente = request.user
        carritos = Carrito.objects.filter(cliente = cliente)

    return render(request, 'productos/consultar.html',{'productos':productos, 'categorias': categorias, 'carritos':carritos})

def consultarPorCategoria_view(request, categoria_id):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(subcategoria__categoria__id = categoria_id)

    if not request.user.is_authenticated:
        carritos = None
    else:
        cliente = request.user
        carritos = Carrito.objects.filter(cliente = cliente)

    return render(request, 'productos/consultar.html',{'productos':productos, 'categorias': categorias, 'carritos':carritos})

def modificarProductos_view(request, codigo):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(codigo = codigo)
    if request.method == 'GET':
        form = FormularioModificarProducto(instance = producto)
    else:
        form = FormularioModificarProducto(request.POST, request.FILES, instance = producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto modificado exitosamente')
        return redirect('productos:consultar')

    return render(request, 'productos/modificar.html', {'form': form, 'categorias': categorias})

def eliminarProducto_view(request, codigo):
    Producto.objects.filter(pk=codigo).delete()
    messages.success(request, 'Producto eliminado exitosamente')
    return redirect('productos:consultar')

def consultarProducto_view(request, codigo):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(codigo=codigo)

    if not request.user.is_authenticated:
        carritos = None
    else:
        cliente = request.user
        carritos = Carrito.objects.filter(cliente = cliente)

    if request.method == 'POST':
        detalle_form = FormularioRegistroDetail(request.POST)
        if detalle_form.is_valid():
            detalle = detalle_form.save(commit = False)
            detalle.producto = producto
            detalle.save()
    else:
        detalle_form = FormularioRegistroDetail()

    return render(request, 'productos/producto.html', {'producto': producto, 'categorias': categorias, 'detalle_form': detalle_form, 'carritos':carritos})

def eliminarDetalle_view(request, id):
    detalle = Detalle.objects.get(pk=id)
    producto = detalle.producto.codigo
    Detalle.objects.filter(pk=id).delete()
    return redirect('productos:consultarProducto', producto)

