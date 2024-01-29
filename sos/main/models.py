from django.db import models
from django.core.validators import MaxLengthValidator

class Ubicacion(models.Model):
    calle = models.TextField()
    colonia = models.TextField()
    codigo = models.IntegerField()
    numero = models.IntegerField()

class Personales(models.Model):
    rfc = models.CharField(max_length=13, primary_key=True, validators=[MaxLengthValidator(limit_value=13)])
    correo = models.EmailField()
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

class Compania(models.Model):
    nombre = models.TextField()
    datos = models.ForeignKey(Personales, on_delete=models.CASCADE)

class Celulares(models.Model):
    modelo = models.TextField()
    manufacturera = models.TextField()
    propietario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    imei = models.TextField(primary_key=True)
    contrasena = models.CharField(max_length=20)
    
class Usuario(models.Model):
    nombre = models.TextField()
    ine = models.TextField(primary_key=True)
    compania = models.ForeignKey(Compania, on_delete=models.CASCADE)
    datos = models.ForeignKey(Personales, on_delete=models.CASCADE)
    
class Reparations(models.Model):
    celular = models.ForeignKey(Celulares, on_delete=models.CASCADE)
    recibido = models.DateField()
    entrega = models.DateField()
    falla = models.TextField()
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reparaciones')
    costo = models.FloatField()
    diagnostico = models.TextField()
