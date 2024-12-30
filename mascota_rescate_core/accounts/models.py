from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """Custom user model with additional fields."""
    
    # Additional fields
    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        verbose_name=_('Imagen de perfil'),
        help_text=_('Sube una imagen de perfil (opcional)')
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name=_('Biografía'),
        help_text=_('Cuéntanos un poco sobre ti (opcional)')
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_('Teléfono'),
        help_text=_('Número de teléfono para contacto (opcional)')
    )
    location = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_('Ubicación'),
        help_text=_('Tu ciudad o región (opcional)')
    )
    
    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
        ordering = ['-date_joined']

    def __str__(self):
        return self.username

    def get_full_name(self):
        """Return the full name of the user."""
        full_name = super().get_full_name()
        return full_name if full_name else self.username

    def get_short_name(self):
        """Return the short name of the user."""
        return self.first_name if self.first_name else self.username
