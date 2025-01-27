from django.shortcuts import render,redirect,get_object_or_404
from .models import Mecanico,Carro,Propietario
from .forms import *

# Create your views here.

def home(request):
    return render(request , 'home.html')

#Mecanico
def mecanico_list(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'mecanico_list.html', {'mecanicos': mecanicos})

def mecanico_create(request):
    if request.method == 'POST':
        form = Mecanico_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mecanico_list')
    else:
        form = Mecanico_form()
    return render(request, 'mecanico_form.html', {'form': form})

def mecanico_update(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        form = Mecanico_form(request.POST, instance=mecanico)
        if form.is_valid():
            form.save()
            return redirect('mecanico_list')
    else:
        form = Mecanico_form(instance=mecanico)
    return render(request, 'mecanico_form.html', {'form': form})

def mecanico_delete(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        mecanico.delete()
        return redirect('mecanico_list')
    return render(request, 'mecanico_confirm_delete.html', {'mecanico': mecanico})

#Carro
def carros_list(request):
    carros = Carro.objects.all()
    return render(request,'carro_list.html',{'carros' : carros})

def carro_create(request):
    if request.method == 'POST':
        form = Carro_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carros_list')
    else:
        form = Carro_form()
    return render(request, 'carro_form.html', {'form': form})

def carro_update(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == 'POST':
        form = Carro_form(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('carros_list')
    else:
        form = Carro_form(instance=carro)
    return render(request, 'carro_form.html', {'form': form})

def carro_delete(request,pk):
    carro = get_object_or_404(Carro,pk = pk)
    if request.method == 'POST':
        carro.delete()
        return redirect('carros_list')
    return render(request, 'carro_confirm_delete.html', {'carro': carro})

#Propietario
def propietario_list(request):
    propietarios = Propietario.objects.all()
    return render(request, 'propietario_list.html',{'propietarios':propietarios})

def propietario_create(request):
    if request.method == 'POST':
        form = Propietario_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propietario_list')
    else:
        form = Propietario_form()
    return render(request,'propietario_form.html',{'form': form})

def propietario_update(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        form = Propietario_form(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('propietario_list')
    else:
        form = Propietario_form(instance=propietario)
    return render(request, 'propietario_form.html', {'form': form})

def propietario_delete(request,pk):
    propietario = get_object_or_404(Propietario,pk = pk)
    if request.method == 'POST':
        propietario.delete()
        return redirect('propietario_list')
    return render(request,'propietario_confirm_delete.html',{'propietario':propietario})