from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

class Mascota(models.Model):
    ESPECIES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('otro', 'Otro'),
    ]
    
    ESTADOS = [
        ('disponible', 'Disponible para adopción'),
        ('adoptado', 'Adoptado'),
        ('en_tratamiento', 'En tratamiento'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIES, default='otro')
    edad = models.IntegerField(default=0)
    unidad_edad = models.CharField(max_length=10, choices=[('meses', 'Meses'), ('años', 'Años')], default='meses')
    descripcion = models.TextField(default='')
    imagen = models.ImageField(upload_to='mascotas/', null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} ({self.get_especie_display()})"

class MascotaImagen(models.Model):
    mascota = models.ForeignKey(Mascota, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='mascotas/')
    es_principal = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"Imagen de {self.mascota.nombre}"