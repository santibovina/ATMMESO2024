from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacion
from .forms import OperacionForm

@login_required
def registrar_operacion(request):
    if request.method == 'POST':
        operacion_form = OperacionForm(request.POST)

        if operacion_form.is_valid():
            operacion = operacion_form.save(commit=False)
            operacion.usuario = request.user  # Asigna el usuario logueado
            operacion.save()
            return redirect('operaciones:lista_operaciones')
    else:
        operacion_form = OperacionForm()

    return render(request, 'operaciones/registrar_operacion.html', {
        'operacion_form': operacion_form
    })

@login_required
def lista_operaciones(request):
    #operaciones = Operacion.objects.filter(usuario=request.user)
    operaciones = Operacion.objects.all()
    return render(request, 'operaciones/lista_operaciones.html', {'operaciones': operaciones})

def home(request):
    return render(request, 'home.html')