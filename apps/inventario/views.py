from django.shortcuts import render, redirect
from .forms import FormularioCantidad
from django.contrib import messages
from .models import Inventario
from django.http import HttpResponseRedirect
#from .models import Categoria

def actualizarCantidad_view(request, id):
    cantidad = int(request.POST["cantidad"])
    if cantidad >= 0:
        inventario = Inventario.objects.get(id=id)
        inventario.cantidad = cantidad
        inventario.save()
    else:
        messages.warning(request, 'Por favor proporcione un numero valido')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                 