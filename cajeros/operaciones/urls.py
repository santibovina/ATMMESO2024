from django.urls import path
from . import views

app_name = 'operaciones'

urlpatterns = [
    path('registrar/', views.registrar_operacion, name='registrar_operacion'),
    path('lista/', views.lista_operaciones, name='lista_operaciones'),
]
