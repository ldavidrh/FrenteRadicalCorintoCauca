import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.db.models import Sum, F
from apps.almacenes.models import Almacen
from apps.productos_vendidos.models import Producto_vendido
from apps.categorias.models import Categoria

# Create your views here.
categorias = Categoria.objects.all()
def productos_mas_vendidos(request):
    mas_vendidos = list(Producto_vendido.objects.select_related('producto__nombre').values(label = F('producto__nombre')).annotate(value = Sum('cantidad_vendida')).order_by('-value')[:20])
    print(mas_vendidos)   
    return render(request, 'reportes/productos_mas_vendidos.html', {'mas_vendidos': mas_vendidos, 'categorias':categorias})
def productos_menos_vendidos(request):
    menos_vendidos = list(Producto_vendido.objects.select_related('producto__nombre').values(label = F('producto__nombre')).annotate(value = Sum('cantidad_vendida')).order_by('value')[:20])
    return render(request, 'reportes/productos_menos_vendidos.html', {'menos_vendidos': menos_vendidos, 'categorias':categorias})

def ventas_por_fecha(request):
    return render(request, 'reportes/ventas_por_fecha.html', {})

def ventas_producto_ultimos_meses(request):
    actual_date = datetime.date.today()
    previous_date = actual_date - relativedelta(months=6)
    actual_date = datetime.date.strftime(actual_date, '%Y-%m-%d')
    previous_date = datetime.date.strftime(previous_date, '%Y-%m-%d')
    
    producto_id = str(id)
    
    ventas_ultimos_meses = list(Producto_vendido.objects.select_related('producto__nombre').filter(factura__fecha__range=[previous_date, actual_date]).values(nombre = F('producto__nombre')).annotate(cantidad = Sum('cantidad_vendida')))
    print(ventas_ultimos_meses)
    return render(request, 'reportes/ventas_producto_ultimos_meses.html', {'ventas_ultimos_meses': ventas_ultimos_meses, 'actual_date':actual_date, 'previous_date': previous_date, 'categorias':categorias})