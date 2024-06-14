from django import forms
from .models import Operacion

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