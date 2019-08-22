from django.shortcuts import render, redirect
from .forms import FormularioRegistroProducto, FormularioModificarProducto, FormularioRegistroDetail
from django.contrib import messages
from .models import Producto
from .models import Detalle
from apps.categorias.models import Categoria
from apps.subcategorias.models import Subcategoria
from django.forms import modelformset_factory

# Create your views here.
def registrar_view(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = FormularioRegistroProducto(request.POST, request.FILES)
        detail_form = FormularioRegistroDetail(request.POST)
        if form.is_valid() and detail_form.is_valid():
            form.save()
            detail_form.save(False)
            messages.success(request, 'Producto registrado exitosamente')
            return redirect('productos:registrar')
    else:
        form = FormularioRegistroProducto()
        detail_form = FormularioRegistroDetail()

    return render(request, 'productos/registro.html', {'form': form,'detail_form': detail_form, 'categorias': categorias})

def consultarProdutos_view(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'productos/consultar.html',{'productos':productos, 'categorias': categorias})

def consultarPorSubcategoria_view(request, subcategoria_id):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(subcategoria_id = subcategoria_id)
    return render(request, 'productos/consultar.html',{'productos':productos, 'categorias': categorias})

def consultarPorCategoria_view(request, categoria_id):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(subcategoria__categoria__id = categoria_id)
    return render(request, 'productos/consultar.html',{'productos':productos, 'categorias': categorias})

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
    return render(request, 'productos/producto.html', {'producto': producto, 'categorias': categorias})


