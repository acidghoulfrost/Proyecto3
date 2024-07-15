from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProductoForm, CustomUserCreationForm
from .models import Producto
from django.contrib.auth import authenticate, login

# Create your views here.

def inicio(request):
    context={}
    return render(request, 'inicio.html', context)

def galeria(request):
    context={}
    return render(request, 'galeria.html', context)

def opinion(request):
    context={}
    return render(request, 'opinion.html', context)

def quienes(request):
    context={}
    return render(request, 'quienes.html', context)

def solicitar(request):
    context={}
    return render(request, 'solicitar.html', context)

def base(request):
    context={}
    return render(request, 'base.html', context)

def login(request):
    context={}
    return render(request, 'login.html', context)

#------------------------------------------------------------

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'actualizar_producto.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="inicio")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

