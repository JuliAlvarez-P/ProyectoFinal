from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile, Mascota, MascotaImagen

class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'email': 'Correo Electrónico'
        }

class PerfilForm(forms.ModelForm):
    imagen = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        })
    )

    class Meta:
        model = Profile
        fields = ['imagen']
        labels = {
            'imagen': 'Foto de Perfil'
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].label = 'Contraseña Actual'
        self.fields['new_password1'].label = 'Nueva Contraseña'
        self.fields['new_password2'].label = 'Confirmar Nueva Contraseña'

class MascotaForm(forms.ModelForm):
    ESTADOS = [
        ('disponible', 'Disponible para adopción'),
        ('adoptado', 'Adoptado'),
        ('en_tratamiento', 'En tratamiento')
    ]
    ESPECIES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('otro', 'Otro')
    ]
    UNIDADES_EDAD = [
        ('meses', 'Meses'),
        ('años', 'Años')
    ]
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    especie = forms.ChoiceField(
        choices=ESPECIES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    edad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0'})
    )
    unidad_edad = forms.ChoiceField(
        choices=UNIDADES_EDAD,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
    estado = forms.ChoiceField(
        choices=ESTADOS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'edad', 'unidad_edad', 'descripcion', 'estado']
        labels = {
            'nombre': 'Nombre',
            'especie': 'Especie',
            'edad': 'Edad',
            'unidad_edad': 'Unidad de edad',
            'descripcion': 'Descripción',
            'estado': 'Estado'
        }

class MascotaImagenForm(forms.ModelForm):
    imagen = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        })
    )
    es_principal = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    class Meta:
        model = MascotaImagen
        fields = ['imagen', 'es_principal']
        labels = {
            'imagen': 'Imagen',
            'es_principal': 'Establecer como imagen principal'
        }
