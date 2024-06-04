from django.db import models
from django.contrib.auth.models import User

class Banco(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Cajero(models.Model):
    id_cajero = models.CharField(max_length=100, unique=True)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id_cajero} - {self.banco} - {self.ubicacion}"

class Gaveta(models.Model):
    id_gaveta = models.CharField(max_length=100, unique=True)
    denominacion_billete = models.DecimalField(max_digits=5, decimal_places=0)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    cajero = models.ForeignKey(Cajero, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id_gaveta} - ${self.denominacion_billete}"

class Operacion(models.Model):
    fecha_operacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateField()
    cajero = models.ForeignKey(Cajero, on_delete=models.CASCADE)
    gaveta = models.ForeignKey(Gaveta, on_delete=models.CASCADE)
    numero_precinto = models.CharField(max_length=100)
    total_por_denominacion = models.DecimalField(max_digits=10, decimal_places=0)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha_operacion.strftime("%d/%m/%Y")} - {self.cajero} - ${self.gaveta.denominacion_billete} - ${self.total_por_denominacion} - {self.gaveta.id_gaveta} - {self.usuario}"
