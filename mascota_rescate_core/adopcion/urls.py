from django.urls import path
from . import views

app_name = 'adopcion'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('mascotas/<int:mascota_id>/', views.detalle_mascota, name='detalle_mascota'),
    path('mascotas/publicar/', views.publicar_mascota, name='publicar_mascota'),
    path('mascotas/<int:pk>/editar/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/<int:pk>/solicitar/', views.solicitar_adopcion, name='solicitar_adopcion'),
    path('como-ayudar/', views.como_ayudar, name='como_ayudar'),
]
