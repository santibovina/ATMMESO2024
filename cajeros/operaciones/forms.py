from django import forms
from .models import Operacion, DetalleGaveta
from django.forms.models import inlineformset_factory

class OperacionForm(forms.ModelForm):
    class Meta:
        model = Operacion
        fields = ['fecha_habilitacion',
                  'cajero',
                  'gaveta',
                  'precinto_gaveta',
                  'total_por_gaveta',
                  'precinto_depurador',
                  'precinto_bolso']