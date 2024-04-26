from django.db import models

class Recetas(models.Model):
    RECETA = '0'
    SALADA = '1'
    DULCE = '2'

    CATEGORIAS = [
        (RECETA, '0'),
        (SALADA, '1'),
        (DULCE, '2'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.IntegerField(choices=CATEGORIAS, default=RECETA)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Saladas(models.Model):
    receta = models.OneToOneField(Recetas, on_delete=models.CASCADE, primary_key=True, default=1)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.receta.nombre

class Dulces(models.Model):
    receta = models.OneToOneField(Recetas, on_delete=models.CASCADE, primary_key=True, default=2)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.receta.nombre



