from django.shortcuts import render, redirect
from apps.almacenes.models import Almacen
from django.http import JsonResponse

# Create your views here.
def get_data(request):
    array = []
    for i in range (5):
        test = {
            'nombre': 'Elemento' + str(i),
            'precio': i * 100
        }
        key = 'el' + str(i)
        array.append(test)
        
    return JsonResponse(array, safe = False)