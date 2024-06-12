from django import forms
from .models import Operacion, DetalleGaveta
from django.forms import inlineformset_factory

class OperacionForm(forms.ModelForm):
    fecha_actualizacion = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y']
    )

    class Meta:
        model = Operacion
        fields = ['fecha_actualizacion', 'cajero']

class DetalleGavetaForm(forms.ModelForm):
    class Meta:
        model = DetalleGaveta
        fields = ['numero_precinto', 'gaveta', 'total_por_gaveta']

DetalleGavetaFormSet = inlineformset_factory(
    Operacion,
    DetalleGaveta,
    form=DetalleGavetaForm,
    extra=1,
    can_delete=True
    )