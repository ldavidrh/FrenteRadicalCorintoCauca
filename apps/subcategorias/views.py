from django.shortcuts import render, redirect
from .forms import FormularioCreacionSubcategoria
from django.contrib import messages
from apps.subcategorias.models import Subcategoria
from apps.categorias.models import Categoria

# Create your views here.
def crear_subcategoria_view(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = FormularioCreacionSubcategoria(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Subcategoria registrada exitosamente')
            redirect('subcategorias:crear_subcategoria')
    else:
        form = FormularioCreacionSubcategoria()
    
    return render(request, 'subcategorias/registro.html', {'form':form, 'categorias': categorias})


def eliminar_subcategoria_view(request, id):
    subcategoria = Subcategoria.objects.filter(pk = id).delete()
    messages.success(request, 'Subcategoria eliminada exitosamente')
    return redirect('categorias:consultar_categorias')

def modificar_subcategoria_view(request, id):
    categorias = Categoria.objects.all()
    subcategoria = Subcategoria.objects.get(id = id)
    if request.method == 'GET':
        form = FormularioCreacionSubcategoria(instance = subcategoria)
    else:
        form = FormularioCreacionSubcategoria(request.POST, instance = subcategoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategoria modifacada exitosamente')
        return redirect('categorias:consultar_categorias')

    return render(request, 'subcategorias/modificar.html', {'form': form, 'categorias': categorias})
