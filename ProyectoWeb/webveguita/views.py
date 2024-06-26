from django.shortcuts import render

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

def login(request):
    context={}
    return render(request, 'login.html', context)

def registro(request):
    context={}
    return render(request, 'registro.html', context)