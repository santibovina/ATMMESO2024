from django import forms
from .models import Operacion, DetalleGaveta
from django.forms.models import inlineformset_factory

class OperacionForm(forms.ModelForm):
    class Meta:
        model = Operacion
        fields = ['fecha_actualizacion',
                  'cajero',
                  'precinto_depurador',
                  'precinto_bolso']
        
class DetalleGavetaForm(forms.ModelForm):
    class Meta:
        model = DetalleGaveta
        fields = ['numero_precinto',
                  'gaveta',
                  'total_por_gaveta']
        
DetalleGavetaFormSet = inlineformset_factory(Operacion, DetalleGaveta, form=DetalleGavetaForm, extra=1, can_delete=True)
        
