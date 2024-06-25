from django import forms
from .models import Operacion, DetalleGaveta

class OperacionForm(forms.ModelForm):

    fecha_habilitacion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y']
    )

    class Meta:
        model = Operacion
        fields = ['fecha_habilitacion',
                  'cajero',
                  'precinto_depurador',
                  'precinto_bolso',
                  'precinto_bolso_2'
                  ]
        # widgets = {
        #     'gaveta': forms.Select(attrs={'class': 'inline-field'}),
        #     'precinto_gaveta': forms.TextInput(attrs={'class': 'inline-field'}),
        #     'total_por_gaveta': forms.NumberInput(attrs={'class': 'inline-field'}),
        # }

class DetalleGavetaForm(forms.ModelForm):
    class Meta:
        model = DetalleGaveta
        fields = ['gaveta',
                  'precinto_gaveta',
                  'total_por_gaveta']

DetalleGavetaFormSet = forms.inlineformset_factory(
    Operacion, DetalleGaveta, form=DetalleGavetaForm, extra=1, can_delete=False
)