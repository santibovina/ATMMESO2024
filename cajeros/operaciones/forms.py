from django import forms
from .models import Operacion

class OperacionForm(forms.ModelForm):

    fecha_habilitacion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y']
    )

    class Meta:
        model = Operacion
        fields = ['fecha_habilitacion',
                  'cajero',
                  'gaveta',
                  'precinto_gaveta',
                  'total_por_gaveta',
                  'gaveta_2',
                  'precinto_gaveta_2',
                  'total_por_gaveta_2',
                  'gaveta_3',
                  'precinto_gaveta_3',
                  'total_por_gaveta_3',
                  'gaveta_4',
                  'precinto_gaveta_4',
                  'total_por_gaveta_4',
                  'precinto_depurador',
                  'precinto_bolso',
                  'precinto_bolso_2',
                  'usuario'
                  ]
        widgets = {
            'gaveta': forms.Select(attrs={'class': 'inline-field'}),
            'precinto_gaveta': forms.TextInput(attrs={'class': 'inline-field'}),
            'total_por_gaveta': forms.NumberInput(attrs={'class': 'inline-field'}),
            'gaveta_2': forms.Select(attrs={'class': 'inline-field'}),
            'precinto_gaveta_2': forms.TextInput(attrs={'class': 'inline-field'}),
            'total_por_gaveta_2': forms.NumberInput(attrs={'class': 'inline-field'}),
            'gaveta_3': forms.Select(attrs={'class': 'inline-field'}),
            'precinto_gaveta_3': forms.TextInput(attrs={'class': 'inline-field'}),
            'total_por_gaveta_3': forms.NumberInput(attrs={'class': 'inline-field'}),
            'gaveta_4': forms.Select(attrs={'class': 'inline-field'}),
            'precinto_gaveta_4': forms.TextInput(attrs={'class': 'inline-field'}),
            'total_por_gaveta_4': forms.NumberInput(attrs={'class': 'inline-field'}),
        }