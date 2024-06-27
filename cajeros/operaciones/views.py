from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacion
from .forms import OperacionForm, DetalleGavetaFormSet
from django.urls import reverse

@login_required
def registrar_operacion(request):
    if request.method == "POST":
        form = OperacionForm(request.POST)
        formset = DetalleGavetaFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            operacion = form.save(commit=False)
            operacion.usuario = request.user  # Asignar el usuario logueado
            operacion.save()
            formset.instance = operacion
            formset.save()
            return redirect(reverse('lista_operaciones'))
    else:
        form = OperacionForm()
        formset = DetalleGavetaFormSet()
    return render(request, 'operaciones/registrar.html', {
        'form': form,
        'formset': formset,
    })

@login_required
def lista_operaciones(request):
    operaciones = Operacion.objects.all()
    return render(request, 'operaciones/lista.html', {'operaciones': operaciones})

def home(request):
    return render(request, 'home.html')