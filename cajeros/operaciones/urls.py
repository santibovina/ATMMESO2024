from django.urls import path
from .views import registrar_operacion, lista_operaciones

app_name = 'operaciones'

urlpatterns = [
    path('registrar/', registrar_operacion, name='registrar_operacion'),
    path('lista/', lista_operaciones, name='lista_operaciones'),
]
