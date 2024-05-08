from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    image = models.ImageField(upload_to='avatars/')
        
    def __str__(self):
        return f"Avatar for {self.user.username}"
    