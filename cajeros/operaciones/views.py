from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OperacionForm
from .models import Operacion

@login_required
def registrar_operacion(request):
    if request.method == 'POST':
        form = OperacionForm(request.POST)
        if form.is_valid():
            operacion = form.save(commit=False)
            operacion.usuario = request.user  # Asignar el usuario logueado
            operacion.save()
            return redirect('operaciones:lista_operaciones')
    else:
        form = OperacionForm()
    return render(request, 'operaciones/registrar_operacion.html', {'form': form})

@login_required
def lista_operaciones(request):
    operaciones = Operacion.objects.filter(usuario=request.user)
    return render(request, 'operaciones/lista_operaciones.html', {'operaciones': operaciones})


def home(request):
    return render(request, 'home.html')