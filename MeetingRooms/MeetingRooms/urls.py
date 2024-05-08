
from django.contrib import admin
from django.urls import path
from bookings import views
from django.conf import settings
from django.conf.urls.static import static
from bookings.views import UserEditView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('crear_personaje/', views.crear_personaje, name='crear_personaje'),
    path('busqueda.html', views.buscar, name='buscar'),
    path('editar_personaje/<int:personaje_id>/', views.editar_personaje, name='editar_personaje'),
    path('borrar_personaje/<int:personaje_id>/', views.borrar_personaje, name='borrar_personaje'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('descripcion/<int:personaje_id>/', views.ver_descripcion, name='descripcion'),
    path('editar_perfil/', UserEditView.as_view(), name='editar_perfil'),
    path('avatar/add', views.avatar_view, name='avatar_add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

