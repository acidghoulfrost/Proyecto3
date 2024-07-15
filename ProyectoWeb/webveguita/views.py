from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistroUserFrom
from django.contrib import messages

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

def login_view(request):
    return render(request, 'login.html')


def registro(request):
    context={}
    return render(request, 'registro.html', context)

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUserFrom(request.POSt)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro con exito! inicia sesion')
            return redirect('login')
    else:
        form = RegistroUserFrom()
    return render(request, 'registro.html', {'form':form})