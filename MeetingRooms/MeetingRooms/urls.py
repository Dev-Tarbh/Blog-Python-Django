
from django.contrib import admin
from django.urls import path
from bookings import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('busqueda.html', views.buscar, name='buscar'),
    path('crear_receta/', views.crear_receta, name='crear_receta'),
    path('editar/<int:receta_id>/', views.editar_receta, name='editar_receta'),
    path('borrar/<int:borrar_id>/', views.borrar_receta, name='borrar_receta'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
