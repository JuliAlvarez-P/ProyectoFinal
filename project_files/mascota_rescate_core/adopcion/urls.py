# adopcion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('lista_mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('como_ayudar/', views.como_ayudar, name='como_ayudar'),
    path('hacer-superusuario/<str:username>/', views.hacer_superusuario, name='hacer_superusuario'),
    path('perfil/', views.perfil, name='perfil'),
    path('mascotas/agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('mascotas/eliminar/<int:mascota_id>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('mascotas/editar/<int:mascota_id>/', views.edit_mascota, name='edit_mascota'),
]
