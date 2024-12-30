from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Form for creating new users."""
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': _('Correo electrónico')
        })
    )
    
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Nombre')
        })
    )
    
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Apellido')
        })
    )
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Nombre de usuario')
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Contraseña')
        })
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Confirmar contraseña')
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class CustomUserChangeForm(forms.ModelForm):
    """Form for updating user profiles."""
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        })
    )
    
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    
    profile_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        }),
        help_text=_('Formatos permitidos: JPG, PNG. Tamaño máximo: 5MB')
    )
    
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': _('Cuéntanos un poco sobre ti...')
        })
    )
    
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Ej: +123456789')
        })
    )
    
    location = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Ej: Ciudad, País')
        })
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'profile_image', 'bio', 'phone', 'location')

    def clean_profile_image(self):
        """Validate the profile image."""
        image = self.cleaned_data.get('profile_image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError(_('La imagen no debe superar los 5MB'))
            if not image.content_type.startswith('image'):
                raise forms.ValidationError(_('El archivo debe ser una imagen'))
        return image
