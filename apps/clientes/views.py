from django.shortcuts import render, redirect
from .forms import FormularioRegistroCliente
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Cliente


# Create your views here.
def registro_view(request):
    if request.method == 'POST':
        form = FormularioRegistroCliente(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            email = form.cleaned_data.get('email')
            instance.username = email
            instance.save()
            messages.success(request, 'Cliente registrado exitosamente')
            return redirect('clientes:login')
    else:
        form = FormularioRegistroCliente()

    return render(request, 'clientes/registro.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'clientes/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
def perfil_view(request, numero_documento):
    try:
        cliente = Cliente.objects.get(usuario_ptr_id=numero_documento)
    except  Cliente.DoesNotExist:
        cliente = None
    
    return render(request, 'clientes/perfil.html', {'cliente': cliente})