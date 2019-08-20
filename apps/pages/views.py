from django.shortcuts import render
from apps.categorias.models import Categoria
from apps.productos.models import Producto
# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos':productos, 'categorias': categorias})
