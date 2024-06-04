from django.contrib import admin
from .models import Cajero, Gaveta, Operacion, Banco

admin.site.register(Banco)
admin.site.register(Cajero)
admin.site.register(Gaveta)
admin.site.register(Operacion)
