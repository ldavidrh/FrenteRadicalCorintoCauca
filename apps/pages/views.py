from django.shortcuts import render
from apps.categorias.models import Categoria
# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'categorias': categorias})
