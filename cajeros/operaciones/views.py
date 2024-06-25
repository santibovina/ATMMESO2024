from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacion
from .forms import OperacionForm, DetalleGavetaFormSet

@login_required
def registrar_operacion(request):
    if request.method == 'POST':
        form = OperacionForm(request.POST)
        formset = DetalleGavetaFormSet(request.POST, instance=form.instance)

        if form.is_valid() and formset.is_valid():
            operacion = form.save()
            detalles = formset.save(commit=False)
            for detalle in detalles:
                detalle.operacion = operacion
                detalle.save()
            return redirect('lista_operaciones')
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