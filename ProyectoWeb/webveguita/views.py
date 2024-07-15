from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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
