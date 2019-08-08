from django.shortcuts import render, redirect
from .forms import FormularioCreacionCategoria
from django.contrib import messages
from .models import Categoria

# Create your views here.


def crear_categoria_view(request):
    if request.method == 'POST':
        form = FormularioCreacionCategoria(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Categoria registrada exitosamente')
            redirect('categorias:crear_categoria')
    else:
        form = FormularioCreacionCategoria()

    return render(request, 'categorias/registro.html', {'form': form})


def consultar_categorias_view(request):
    categorias = Categoria.objects.all().values()
    return render(request, 'categorias/consultar.html', {'categorias': categorias})


def eliminar_categoria_view(request, id):
    Categoria.objects.filter(pk=id).delete()
    return redirect('categorias:consultar_categorias')


def modificar_categoria_view(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'GET':
        form = FormularioCreacionCategoria(instance = categoria)
    else:
        form = FormularioCreacionCategoria(request.POST, instance = categoria)
        if form.is_valid():
            form.save()
        return redirect('categorias:consultar_categorias')

    return render(request, 'categorias/modificar.html', {'form': form})
