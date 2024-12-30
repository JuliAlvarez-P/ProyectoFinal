from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser
from .models import Mascota, SolicitudAdopcion

class MascotaForm(forms.ModelForm):
    """Formulario para crear y editar mascotas."""
    
    class Meta:
        model = Mascota
        fields = ['nombre', 'tipo', 'raza', 'edad', 'sexo', 'tamanio', 'descripcion', 'foto']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
        # Add help text for image field
        self.fields['foto'].help_text = _('Formatos permitidos: JPG, PNG. Tamaño máximo: 5MB')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class SolicitudAdopcionForm(forms.ModelForm):
    """Formulario para solicitudes de adopción."""
    
    class Meta:
        model = SolicitudAdopcion
        fields = ['motivo', 'experiencia_previa', 'vivienda', 'tiene_patio', 'otros_animales']
        widgets = {
            'motivo': forms.Textarea(attrs={'rows': 4}),
            'experiencia_previa': forms.Textarea(attrs={'rows': 4}),
            'otros_animales': forms.Textarea(attrs={'rows': 4}),
            'vivienda': forms.TextInput(attrs={'placeholder': _('Ej: Casa, Departamento, etc.')}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'
