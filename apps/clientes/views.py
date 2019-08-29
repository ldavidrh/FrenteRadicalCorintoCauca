from django.shortcuts import render, redirect
from .forms import FormularioModificarCliente, FormularioModificarCuenta, FormularioRegistroCliente
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout
from .models import Cliente
from ..usuarios.models import Usuario
from apps.categorias.models import Categoria


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
    categorias = Categoria.objects.all()
    try:
        cliente = Cliente.objects.get(usuario_ptr_id=numero_documento)
    except  Cliente.DoesNotExist:
        cliente = Usuario.objects.get(numero_documento=numero_documento)

    if request.method == 'POST':
        if cliente.is_staff:
            form = FormularioModificarCuenta(request.POST, instance=cliente)
        else:
            form = FormularioModificarCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cambios guardados exitosamente')
        return redirect('clientes:perfil', numero_documento)

    else:
        if cliente.is_staff:
            form = FormularioModificarCuenta(instance=cliente)
        else:
            form = FormularioModificarCliente(instance=cliente) 
            
    return render(request, 'clientes/perfil.html', {'form':form, 'cliente': cliente, 'categorias': categorias})

def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cambios guardados exitosamente')
            return redirect('clientes:login')
        else:
            return redirect('clientes:change_password')
    else:
        form = PasswordChangeForm(user= request.user)
        return render(request, 'clientes/change_password.html', {'form':form})

def eliminarCuenta_view(request, numero_documento):
    usuario = Usuario.objects.get(numero_documento=numero_documento)
    if request.method == 'GET':
        usuario.is_active = 'f'
        usuario.save()
        messages.success(request, 'Cuenta eliminada exitosamente')
        usuario = request.user
        if usuario.is_staff:
            return redirect('clientes:consulta')
        else:
            return redirect('home')

def consultarClientes_view(request):
    categorias = Categoria.objects.all()
    clientes = Cliente.objects.filter(is_staff='f', is_superuser='f')
    return render(request, 'clientes/consultar.html', {'clientes': clientes, 'categorias': categorias})

def activarCliente_view(request, numero_documento):
    usuario = Usuario.objects.get(numero_documento=numero_documento)
    if request.method == 'GET':
        usuario.is_active = 't'
        usuario.save()
        messages.success(request, 'Cuenta reactivada exitosamente')
        return redirect('clientes:consulta')




