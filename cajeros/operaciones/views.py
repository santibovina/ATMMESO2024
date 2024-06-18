from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacion
from .forms import OperacionForm, DetalleGavetaFormSet, PrecintoBolsoFormSet

# operaciones/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OperacionForm, DetalleGavetaFormSet, PrecintoBolsoFormSet

@login_required
def registrar_operacion(request):
    if request.method == 'POST':
        form = OperacionForm(request.POST)
        formset = DetalleGavetaFormSet(request.POST)
        precinto_bolso_formset = PrecintoBolsoFormSet(request.POST)
        if form.is_valid() and formset.is_valid() and precinto_bolso_formset.is_valid():
            operacion = form.save(commit=False)
            operacion.usuario = request.user
            operacion.save()
            detalles = formset.save(commit=False)
            for detalle in detalles:
                detalle.operacion = operacion
                detalle.save()
            precintos = precinto_bolso_formset.save(commit=False)
            for precinto in precintos:
                precinto.operacion = operacion
                precinto.save()
            return redirect('operaciones:lista_operaciones')
    else:
        form = OperacionForm()
        formset = DetalleGavetaFormSet()
        precinto_bolso_formset = PrecintoBolsoFormSet()
    return render(request, 'operaciones/registrar_operacion.html', {'form': form, 'formset': formset, 'precinto_bolso_formset': precinto_bolso_formset})

@login_required
def lista_operaciones(request):
    operaciones = Operacion.objects.filter(usuario=request.user)
    return render(request, 'operaciones/lista_operaciones.html', {'operaciones': operaciones})

def home(request):
    return render(request, 'home.html')