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
    
class Billete(models.Model):
    billete_denominacion = models.IntegerField()

    def __str__(self):
        return f"${self.billete_denominacion}"

class Modelo(models.Model):
    modelo_gaveta = models.CharField(max_length=255)

    def __str__(self):
        return self.modelo_gaveta
    
class Tipologia(models.Model):
    tipologia_gaveta = models.CharField(max_length=255)

    def __str__(self):
        return self.tipologia_gaveta

class Gaveta(models.Model):
    id_gaveta = models.CharField(max_length=100, unique=True)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    denominacion_billete = models.ForeignKey(Billete, on_delete=models.CASCADE)
    modelo_atm = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, blank=True)
    tipologia = models.ForeignKey(Tipologia, on_delete=models.CASCADE, null=True, blank=True)
    cajero = models.ForeignKey(Cajero, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id_gaveta} - {self.modelo_atm} - {self.tipologia} - {self.denominacion_billete}"

class Operacion(models.Model):
    fecha_operacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateField()
    cajero = models.ForeignKey(Cajero, on_delete=models.CASCADE)
    gaveta = models.ForeignKey(Gaveta, on_delete=models.CASCADE)
    numero_precinto = models.CharField(max_length=100, unique=True)
    # billete = models.ForeignKey(Billete, on_delete=models.CASCADE, null=True, blank=True)
    total_por_gaveta = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha_operacion.strftime("%d/%m/%Y")} - {self.cajero} - ${self.gaveta.denominacion_billete} - ${self.total_por_gaveta} - {self.gaveta.id_gaveta} - {self.usuario}"
    
class TipoDiferencia(models.Model):
    tipo_diferencia = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_diferencia
    
class Portavalor(models.Model):
    id_portavalor = models.CharField(max_length=10, unique=True)
    nombre_portavalor = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id_portavalor} - {self.nombre_portavalor}"
    
class Diferencias(models.Model):
    cajero = models.ForeignKey(Cajero, on_delete=models.CASCADE)
    fecha_actualizacion = models.DateField()
    tipo_diferencia = models.ForeignKey(TipoDiferencia, on_delete=models.CASCADE)
    recorrido = models.IntegerField()
    portavalor = models.ForeignKey(Portavalor, on_delete=models.CASCADE)
    total_diferencia = models.IntegerField()
    observaciones = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fecha} - {self.cajero} - {self.tipo_diferencia} - {self.total_diferencia} - {self.observaciones} - {self.portavalor}"