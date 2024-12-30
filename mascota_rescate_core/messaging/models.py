from django.db import models
from django.conf import settings
from django.utils import timezone

class Message(models.Model):
    """Model for handling user-to-user messages."""
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='sent_messages',
        on_delete=models.CASCADE,
        verbose_name='Remitente'
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='received_messages',
        on_delete=models.CASCADE,
        verbose_name='Destinatario'
    )
    content = models.TextField(
        verbose_name='Contenido',
        help_text='Escribe tu mensaje aquí'
    )
    timestamp = models.DateTimeField(
        default=timezone.now,
        verbose_name='Fecha y hora'
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name='Leído'
    )

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['-timestamp']),
            models.Index(fields=['sender', 'receiver']),
        ]

    def __str__(self):
        return f'Mensaje de {self.sender} para {self.receiver}'

    def mark_as_read(self):
        """Mark the message as read if it hasn't been read yet."""
        if not self.is_read:
            self.is_read = True
            self.save(update_fields=['is_read'])
