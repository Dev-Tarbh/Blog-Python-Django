
from django.contrib import admin
from django.urls import path
from bookings import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('busqueda.html', views.buscar, name='buscar'),
    path('crear_receta/', views.crear_receta, name='crear_receta')
]
