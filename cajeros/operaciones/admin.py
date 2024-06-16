from django.contrib import admin
from .models import Cajero, Gaveta, RedAtm, Operacion, Banco, Billete, Modelo, Tipologia, TipoDiferencia, Portavalor, Diferencias

class OperacionesAdmin(admin.ModelAdmin):
    search_fields = ['precinto_gaveta', 'precinto_bolso']
    list_filter = ['cajero', 'fecha_habilitacion']
    list_per_page = 20


admin.site.register(Banco)
admin.site.register(Cajero)
admin.site.register(RedAtm)
admin.site.register(Gaveta)
admin.site.register(Operacion, OperacionesAdmin)
admin.site.register(Billete)
admin.site.register(Modelo)
admin.site.register(Tipologia)
admin.site.register(TipoDiferencia)
admin.site.register(Portavalor)
admin.site.register(Diferencias)
