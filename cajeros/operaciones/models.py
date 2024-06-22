from django.db import models
from django.contrib.auth.models import User

# python manage.py makemigrations <----- lee el archivo models y crea un archivo de migracio
# python manage.py migrate <----- toma las migraciones pendientes y las vuelca en las BBDD

class Banco(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class RedAtm(models.Model):
    red_atm = models.CharField(max_length=10)

    def __str__(self):
        return self.red_atm

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

class Cajero(models.Model):
    id_cajero = models.CharField(max_length=100, unique=True)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    red_atm = models.ForeignKey(RedAtm, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return f"Id: {self.id_cajero} | Banco: {self.banco} | Red: {self.red_atm} | Ubicación: {self.ubicacion}"
    
class Gaveta(models.Model):
    id_gaveta = models.CharField(max_length=10, unique=True)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    denominacion_billete = models.ForeignKey(Billete, on_delete=models.CASCADE)
    modelo_atm = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, blank=True)
    tipologia = models.ForeignKey(Tipologia, on_delete=models.CASCADE, null=True, blank=True)
    cajero = models.ForeignKey(Cajero, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id_gaveta} - {self.modelo_atm} - {self.tipologia} - {self.denominacion_billete}"

class Operacion(models.Model):
    fecha_operacion = models.DateTimeField(auto_now_add=True)
    fecha_habilitacion = models.DateField()
    cajero = models.ForeignKey(Cajero, on_delete=models.CASCADE, verbose_name="ATM")
    #gaveta = models.ForeignKey(Gaveta, on_delete=models.CASCADE)
    #precinto_gaveta = models.CharField(max_length=15, unique=True)
    #total_por_gaveta = models.IntegerField()
    precinto_depurador = models.CharField(max_length=15, unique=True, null=True, blank=True)
    #precinto_bolso = models.CharField(max_length=15, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return f"Fecha habilitación: {self.fecha_habilitacion.strftime("%d/%m/%Y")} | Id cajero: {self.cajero.id_cajero} | Banco: {self.cajero.banco} | Denominación: {self.gaveta.denominacion_billete} | Total gaveta 1: ${self.total_por_gaveta} | Fecha carga: {self.fecha_operacion.strftime("%d/%m/%Y")} por {self.usuario}"
        return f"Operación {self.id} - {self.cajero}"
    
class DetalleGaveta(models.Model):
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE, related_name='detalles_gaveta')
    gaveta = models.ForeignKey(Gaveta, on_delete=models.CASCADE)
    precinto_gaveta = models.CharField(max_length=15, unique=True)
    total_por_gaveta = models.IntegerField()

    # def __str__(self):
    #     return f"Gaveta: {self.gaveta.id_gaveta} | Total de gaveta: ${self.total_por_gaveta}"
    
class PrecintoBolso(models.Model):
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE, related_name='precintos_bolso')
    precinto_bolso = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.precinto_bolso
    
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