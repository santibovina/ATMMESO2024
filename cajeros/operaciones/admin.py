from django.contrib import admin
from .models import Cajero, Gaveta, Operacion, Banco, Billete, Modelo, Tipologia, TipoDiferencia, Portavalor, Diferencias

admin.site.register(Banco)
admin.site.register(Cajero)
admin.site.register(Gaveta)
admin.site.register(Operacion)
admin.site.register(Billete)
admin.site.register(Modelo)
admin.site.register(Tipologia)
admin.site.register(TipoDiferencia)
admin.site.register(Portavalor)
admin.site.register(Diferencias)
