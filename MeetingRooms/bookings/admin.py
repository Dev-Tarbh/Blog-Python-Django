from django.contrib import admin
from .models import Personajes, Fecha, Avatar

# Register your models here.
admin.site.register(Personajes)
admin.site.register(Fecha)
admin.site.register(Avatar)