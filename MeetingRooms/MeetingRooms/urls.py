
from django.contrib import admin
from django.urls import path
from bookings import views
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('busqueda.html', views.busqueda, name='buscar')
]
