import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.db.models import Sum, F
from django.db.models.functions import Extract
from apps.almacenes.models import Almacen
from apps.productos_vendidos.models import Producto_vendido
from apps.categorias.models import Categoria
from apps.inventario.models import Inventario
from apps.usuarios.models import Usuario

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
    fecha_actual = datetime.date.today()
    fecha_previa = fecha_actual - relativedelta(months=6)
    fecha_actual = datetime.date.strftime(fecha_actual, '%Y-%m-%d')
    fecha_previa = datetime.date.strftime(fecha_previa, '%Y-%m-%d')
    
    producto_id = str(id)
    
    ventas_ultimos_meses = list(Producto_vendido.objects.select_related('producto__nombre').filter(factura__fecha__range=[fecha_previa, fecha_actual]).values(nombre = F('producto__nombre')).annotate(cantidad = Sum('cantidad_vendida')))
 
    return render(request, 'reportes/ventas_producto_ultimos_meses.html', {'ventas_ultimos_meses': ventas_ultimos_meses, 'fecha_actual':fecha_actual, 'fecha_previa': fecha_previa, 'categorias':categorias})

def productos_baja_existencia(request):
    existencia_productos = Inventario.objects.select_related('almacen__ciudad', 'producto__nombre').values(almacen_ciudad = F('almacen__ciudad'), nombre_producto = F('producto__nombre')).annotate(cantidad_producto = Sum('cantidad')).filter(cantidad_producto__lte=10).order_by('almacen_ciudad')
    return render(request, 'reportes/baja_existencia.html', {'existencia_productos':existencia_productos, 'categorias':categorias})

def aniversarios_mes_siguiente(request):
    mes_actual = datetime.date.today().month
    mes_siguiente = mes_actual + 1

    aniversarios_clientes_mes_siguiente = Usuario.objects.values('first_name', 'last_name', 'tipo_documento', 'numero_documento', 'fecha_nacimiento').annotate(mes_nacimiento=Extract('fecha_nacimiento', 'month')).filter(mes_nacimiento=mes_siguiente, is_staff='f', is_superuser='f')
    print(aniversarios_clientes_mes_siguiente)
    return render(request, 'reportes/aniversarios_mes_siguiente.html', {'aniversarios_clientes_mes_siguiente':aniversarios_clientes_mes_siguiente, 'categorias':categorias})
    