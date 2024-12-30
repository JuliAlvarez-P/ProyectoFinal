from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import os

def mascota_imagen_path(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    # Create a new filename with timestamp
    filename = f"{instance.nombre}_{timezone.now().strftime('%Y%m%d_%H%M%S')}.{ext}"
    # Return the upload path
    return os.path.join('mascotas', filename)

class Mascota(models.Model):
    """Modelo para mascotas en adopción."""
    
    TIPO_CHOICES = [
        ('perro', _('Perro')),
        ('gato', _('Gato')),
        ('otro', _('Otro')),
    ]
    
    SEXO_CHOICES = [
        ('M', _('Macho')),
        ('H', _('Hembra')),
    ]
    
    TAMANIO_CHOICES = [
        ('P', _('Pequeño')),
        ('M', _('Mediano')),
        ('G', _('Grande')),
    ]
    
    nombre = models.CharField(
        max_length=100,
        verbose_name=_('Nombre'),
        help_text=_('Nombre de la mascota')
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        default='perro',
        verbose_name=_('Tipo'),
        help_text=_('Tipo de mascota')
    )
    raza = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_('Raza'),
        help_text=_('Raza de la mascota (opcional)')
    )
    edad = models.PositiveIntegerField(
        verbose_name=_('Edad'),
        help_text=_('Edad en años'),
        default=1
    )
    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        default='M',
        verbose_name=_('Sexo'),
        help_text=_('Sexo de la mascota')
    )
    tamanio = models.CharField(
        max_length=1,
        choices=TAMANIO_CHOICES,
        default='M',
        verbose_name=_('Tamaño'),
        help_text=_('Tamaño de la mascota')
    )
    descripcion = models.TextField(
        verbose_name=_('Descripción'),
        help_text=_('Descripción detallada de la mascota')
    )
    foto = models.ImageField(
        upload_to=mascota_imagen_path,
        verbose_name=_('Foto'),
        help_text=_('Foto de la mascota'),
        null=True,
        blank=True
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Usuario'),
        help_text=_('Usuario que publica la mascota')
    )
    fecha_registro = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Fecha de registro')
    )
    adoptada = models.BooleanField(
        default=False,
        verbose_name=_('Adoptada'),
        help_text=_('Indica si la mascota ya fue adoptada')
    )
    
    class Meta:
        verbose_name = _('Mascota')
        verbose_name_plural = _('Mascotas')
        ordering = ['-fecha_registro']
    
    def __str__(self):
        return self.nombre

class SolicitudAdopcion(models.Model):
    """Modelo para solicitudes de adopción."""
    
    ESTADO_CHOICES = [
        ('P', _('Pendiente')),
        ('A', _('Aprobada')),
        ('R', _('Rechazada')),
    ]
    
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        verbose_name=_('Mascota'),
        related_name='solicitudes'
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Usuario'),
        related_name='solicitudes_adopcion'
    )
    motivo = models.TextField(
        verbose_name=_('Motivo'),
        help_text=_('¿Por qué quieres adoptar esta mascota?')
    )
    experiencia_previa = models.TextField(
        verbose_name=_('Experiencia previa'),
        help_text=_('¿Has tenido mascotas antes? Cuéntanos tu experiencia.')
    )
    vivienda = models.CharField(
        max_length=50,
        verbose_name=_('Tipo de vivienda'),
        help_text=_('¿En qué tipo de vivienda vives? (casa, departamento, etc.)')
    )
    tiene_patio = models.BooleanField(
        default=False,
        verbose_name=_('¿Tiene patio?'),
        help_text=_('¿Tu vivienda cuenta con patio?')
    )
    otros_animales = models.TextField(
        blank=True,
        verbose_name=_('Otros animales'),
        help_text=_('¿Tienes otras mascotas? Cuéntanos sobre ellas.')
    )
    fecha_solicitud = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Fecha de solicitud')
    )
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES,
        default='P',
        verbose_name=_('Estado')
    )
    
    class Meta:
        verbose_name = _('Solicitud de adopción')
        verbose_name_plural = _('Solicitudes de adopción')
        ordering = ['-fecha_solicitud']
    
    def __str__(self):
        return f'{self.usuario.username} - {self.mascota.nombre}'
