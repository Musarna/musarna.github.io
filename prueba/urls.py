from django.contrib import admin
from django.urls import path,include
from pruebaApp import views as vista
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from pruebaAPI import views as vistasApi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vista.inicio,name='inicio'),
    path("juguete/",vista.crear_juguete,name='juguete'),
    path("juguetes/",vista.mostrar_juguetes,name='juguetes'),
    path('juguete/<int:id>/',vista.juguete_detalles, name='juguete_detalles'),
    path("jugueteEdit/<int:juguete_id>",vista.cargar_editar_juguetes,name='editarJuguete'),
    path("jugueteEditado/<int:juguete_id>",vista.editar_juguete,name='jugueteEditado'),
    path("jugueteDel/<int:juguete_id>",vista.eliminar_juguete,name='jugueteDel'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('registro/', vista.registrar_usuario, name='registro'),  # Ruta para el registro

    path('juguetesAPI/', vistasApi.juguetesApi,name = 'juguetesAPI'),
    path('juguetesListApi/',vistasApi.juguete_listado,name = 'empleadosListApi'),
    path('juguetesListApi/<int:pk>',vistasApi.juguete_detalle,name = 'empleadosListApi'),


]
#lol
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)