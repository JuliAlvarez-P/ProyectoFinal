from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Admin configuration for Message model."""
    list_display = ('sender', 'receiver', 'short_content', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')
    date_hierarchy = 'timestamp'
    readonly_fields = ('timestamp',)
    
    def short_content(self, obj):
        """Return truncated content for list display."""
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    short_content.short_description = 'Contenido'

    fieldsets = (
        ('Información del Mensaje', {
            'fields': ('sender', 'receiver', 'content')
        }),
        ('Estado', {
            'fields': ('is_read', 'timestamp')
        }),
    )
