from django.db import models

# Create your models here.

class Aves(models.Model):
    orden = models.CharField(max_length=200)
    familia = models.CharField(max_length=200)
    especie = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    caracteristicas = models.TextField()
    ultima_observacion = models.DateField()
    foto = models.ImageField(upload_to='bird_photos/', blank = True, null = True)
    
    def __str__(self):
        return f"{self.nombre} - {self.especie}"
    
class Flora(models.Model):
    especie = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    caracteristicas = models.TextField()
    
    def __str__(self):
        return f"{self.nombre} - {self.especie}"
    
class Fauna(models.Model):
    orden = models.CharField(max_length=200)
    familia = models.CharField(max_length=200)
    especie = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    caracteristicas = models.TextField()
    ultima_observacion = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} - {self.especie}"
    
