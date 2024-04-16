from django.db import models

class Recetas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'bookings'

class Saladas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Recetas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'bookings'

class Dulces(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default='')  # Valor predeterminado para el campo 'descripcion'
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Recetas, on_delete=models.CASCADE, default=1)  # Valor predeterminado para el campo 'categoria'

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'bookings'
