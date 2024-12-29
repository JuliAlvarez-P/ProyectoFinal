from django.contrib import admin
from .models import Mascota

# Register your models here.

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'descripcion')
    list_filter = ('edad',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'edad')
        }),
        ('Detalles', {
            'fields': ('descripcion', 'imagen')
        }),
    )
