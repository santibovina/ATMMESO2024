from django.db import models
from django.contrib.auth.models import User

class Cajero(models.Model):
    id_cajero = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.id_cajero

class Gaveta(models.Model):
    id_gaveta = models.CharField(max_length=100, unique=True)
    denominacion_billete = models.DecimalField(max_digits=10, decimal_places=2)
    banco = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id_gaveta} - {self.denominacion_billete}"

class Operacion(models.Model):
    fecha_operacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateField()
    cajero = models.ForeignKey(Cajero, on_delete=models.CASCADE)
    gaveta = models.ForeignKey(Gaveta, on_delete=models.CASCADE)
    numero_precinto = models.CharField(max_length=100)
    total_por_denominacion = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Operación {self.id} en {self.fecha_operacion}"
