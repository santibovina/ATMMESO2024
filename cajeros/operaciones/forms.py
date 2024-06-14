from django import forms
from .models import Operacion, Cajero, Gaveta

class OperacionForm(forms.ModelForm):
    class Meta:
        model = Operacion
        fields = ['fecha_habilitacion', 'cajero', 'precinto_gaveta', 'gaveta', 'total_por_gaveta',]
        
    # def clean(self):
    #     cleaned_data = super().clean()
    #     gaveta = cleaned_data.get("gaveta")
    #     total_por_denominacion = cleaned_data.get("total_por_denominacion")

    #     if gaveta and total_por_denominacion:
    #         if gaveta.denominacion_billete != total_por_denominacion:
    #             raise forms.ValidationError("La denominación del billete no coincide con la de la gaveta.")
    #     return cleaned_data
