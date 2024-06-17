from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OperacionForm, DetalleGavetaFormSet

@login_required
def registrar_operacion(request):
    if request.method == 'POST':
        form = OperacionForm(request.POST)
        formset = DetalleGavetaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            operacion = form.save(commit=False)
            operacion.usuario = request.user
            operacion.save()
            detalles = formset.save(commit=False)
            for detalle in detalles:
                detalle.operacion = operacion
                detalle.save()
            return redirect('operaciones:lista_operaciones')
    else:
        form = OperacionForm()
        formset = DetalleGavetaFormSet()
    return render(request, 'operaciones/registrar_operacion.html', {'form': form, 'formset': formset})

@login_required
def lista_operaciones(request):
    operaciones = Operacion.objects.filter(usuario=request.user)
    return render(request, 'operaciones/lista_operaciones.html', {'operaciones': operaciones})

def home(request):
    return render(request, 'home.html')