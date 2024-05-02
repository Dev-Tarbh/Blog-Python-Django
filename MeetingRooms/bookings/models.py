from django.db import models
from django.utils import timezone

class Fecha(models.Model):
    nombre = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = "Fecha"
        verbose_name_plural = "Fechas"
        
class Personajes(models.Model):
    nombre = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre