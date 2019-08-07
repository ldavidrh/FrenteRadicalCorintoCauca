from django.shortcuts import render, redirect
from .forms import FormularioRegistroProducto
from django.contrib import messages

# Create your views here.

def productos_view(request):
    if request.method == 'POST':
