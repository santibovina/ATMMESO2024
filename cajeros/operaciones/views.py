from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacion
from .forms import OperacionForm, DetalleGavetaFormSet, PrecintoBolsoFormSet

@login_required
def registrar_operacion(request):
    if request.method == 'POST':
        operacion_form = OperacionForm(request.POST)
        detalle_gaveta_formset = DetalleGavetaFormSet(request.POST, request.FILES)
        precinto_bolso_formset = PrecintoBolsoFormSet(request.POST, request.FILES)

        if operacion_form.is_valid() and detalle_gaveta_formset.is_valid() and precinto_bolso_formset.is_valid():
            operacion = operacion_form.save(commit=False)
            operacion.usuario = request.user  # Asigna el usuario logueado
            operacion.save()

            detalle_gaveta_formset.instance = operacion
            detalle_gaveta_formset.save()

            precinto_bolso_formset.instance = operacion
            precinto_bolso_formset.save()

            return redirect('operaciones:lista_operaciones')
    else:
        operacion_form = OperacionForm()
        detalle_gaveta_formset = DetalleGavetaFormSet()
        precinto_bolso_formset = PrecintoBolsoFormSet()

    return render(request, 'operaciones/registrar_operacion.html', {
        'operacion_form': operacion_form,
        'detalle_gaveta_formset': detalle_gaveta_formset,
        'precinto_bolso_formset': precinto_bolso_formset,
    })

@login_required
def lista_operaciones(request):
    #operaciones = Operacion.objects.filter(usuario=request.user)
    operaciones = Operacion.objects.all()
    return render(request, 'operaciones/lista_operaciones.html', {'operaciones': operaciones})

def home(request):
    return render(request, 'home.html')