from django.db import models

class Recetas(models.Model):
    RECETA = 'recetas'
    SALADA = 'saladas'
    DULCE = 'dulces'

    CATEGORIAS = [
        (RECETA, 'recetas'),
        (SALADA, 'saladas'),
        (DULCE, 'dulces'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.IntegerField(choices=CATEGORIAS, default=RECETA)
    imagen = models.ImageField(upload_to='receta/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Saladas(models.Model):
    receta = models.OneToOneField(Recetas, on_delete=models.CASCADE, primary_key=True, default=1)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.receta.nombre

class Dulces(models.Model):
    receta = models.OneToOneField(Recetas, on_delete=models.CASCADE, primary_key=True, default=2)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.receta.nombre



