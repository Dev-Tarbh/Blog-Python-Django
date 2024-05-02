
from django.contrib import admin
from django.urls import path
from bookings import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('crear_personaje/', views.crear_personaje, name='crear_personaje'),
    path('busqueda.html', views.buscar, name='buscar'),
    path('editar_personaje/<int:personaje_id>/', views.editar_personaje, name='editar_personaje'),
    path('borrar_personaje/<int:personaje_id>/', views.borrar_personaje, name='borrar_personaje'),
    #path('crear_usuario/', user_creation_view, name='crear-usuario'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
] 
