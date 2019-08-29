from django.shortcuts import render
from apps.categorias.models import Categoria
from apps.productos.models import Producto
from apps.carritos.models import Carrito
from apps.almacenes.forms import FormularioCiudad
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
    return render(request, 'home.html', {'productos':productos, 'categorias': categorias, 'form_ciudades': form_ciudades, 'carritos':carritos})
