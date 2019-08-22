from django.shortcuts import render
from apps.categorias.models import Categoria
from apps.productos.models import Producto
from apps.almacenes.forms import FormularioCiudad
# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    form_ciudades = FormularioCiudad()
    return render(request, 'home.html', {'productos':productos, 'categorias': categorias, 'form_ciudades': form_ciudades})
