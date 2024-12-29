from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash
from .models import Mascota, Profile, MascotaImagen
from .forms import RegistroForm, PerfilForm, MascotaForm, CustomPasswordChangeForm, UserUpdateForm, MascotaImagenForm

def inicio(request):
    # Datos de ejemplo para las mascotas destacadas
    mascotas_destacadas = [
        {
            'nombre': 'Max',
            'tipo': 'Perro',
            'descripcion': 'Fiel compañero esperando por ti',
            'imagen': 'https://images.unsplash.com/photo-1517849845537-4d257902454a'
        },
        {
            'nombre': 'Luna',
            'tipo': 'Gato',
            'descripcion': 'Elegante felina busca familia',
            'imagen': 'https://images.unsplash.com/photo-1573865526739-10659fec78a5'
        },
        {
            'nombre': 'Rocky',
            'tipo': 'Cachorro',
            'descripcion': 'Pequeño travieso lleno de energía',
            'imagen': 'https://images.unsplash.com/photo-1601758124510-52d02ddb7cbd'
        }
    ]
    
    return render(request, 'adopcion/inicio.html', {
        'mascotas_destacadas': mascotas_destacadas,
        'titulo_pagina': 'Inicio - Mascotas Rescate'
    })

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion')
    else:
        form = RegistroForm()
    return render(request, 'adopcion/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
    return render(request, 'adopcion/iniciar_sesion.html')

def es_administrador(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(es_administrador)
def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.creado_por = request.user
            mascota.save()
            messages.success(request, 'Mascota agregada exitosamente')
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'adopcion/agregar_mascota.html', {'form': form})

@user_passes_test(es_administrador)
def eliminar_mascota(request, mascota_id):
    try:
        mascota = Mascota.objects.get(id=mascota_id)
        mascota.delete()
        messages.success(request, 'Mascota eliminada exitosamente')
    except Mascota.DoesNotExist:
        messages.error(request, 'Mascota no encontrada')
    return redirect('lista_mascotas')

@login_required
@user_passes_test(es_administrador)
def edit_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        imagen_form = MascotaImagenForm(request.POST, request.FILES)
        
        if form.is_valid():
            mascota = form.save()
            
            # Handle image uploads
            if request.FILES.getlist('imagen'):
                for img in request.FILES.getlist('imagen'):
                    MascotaImagen.objects.create(
                        mascota=mascota,
                        imagen=img,
                        es_principal=False
                    )
            
            # Handle image deletions
            imagenes_a_eliminar = request.POST.getlist('eliminar_imagen')
            if imagenes_a_eliminar:
                MascotaImagen.objects.filter(id__in=imagenes_a_eliminar).delete()
            
            # Handle principal image
            nueva_principal = request.POST.get('imagen_principal')
            if nueva_principal:
                MascotaImagen.objects.filter(mascota=mascota).update(es_principal=False)
                MascotaImagen.objects.filter(id=nueva_principal).update(es_principal=True)
            
            messages.success(request, 'Mascota actualizada exitosamente.')
            return redirect('lista_mascotas')
    else:
        form = MascotaForm(instance=mascota)
        imagen_form = MascotaImagenForm()
    
    return render(request, 'adopcion/edit_mascota.html', {
        'form': form,
        'imagen_form': imagen_form,
        'mascota': mascota,
        'imagenes': mascota.imagenes.all().order_by('-es_principal', 'orden')
    })

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    es_admin = request.user.is_authenticated and request.user.is_staff
    return render(request, 'adopcion/lista_mascotas.html', {
        'mascotas': mascotas,
        'es_admin': es_admin
    })

def hacer_superusuario(request, username):
    if request.user.is_superuser:
        try:
            user = User.objects.get(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request, f'Usuario {username} ahora es superusuario')
        except User.DoesNotExist:
            messages.error(request, f'Usuario {username} no existe')
    return redirect('inicio')

@login_required
def perfil(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        if 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, 'Tu contraseña ha sido actualizada exitosamente.')
                return redirect('perfil')
            else:
                messages.error(request, 'Por favor corrige los errores en el formulario de contraseña.')
                user_form = UserUpdateForm(instance=request.user)
                profile_form = PerfilForm(instance=profile)
        else:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            if 'imagen' in request.FILES:
                profile_form = PerfilForm(request.POST, request.FILES, instance=profile)
            else:
                profile_form = PerfilForm(request.POST, instance=profile)
            
            if user_form.is_valid():
                user = user_form.save()
                if 'imagen' in request.FILES and profile_form.is_valid():
                    profile_form.save()
                messages.success(request, 'Perfil actualizado exitosamente')
                # Force refresh by redirecting
                return redirect('perfil')
            else:
                messages.error(request, 'Por favor corrige los errores en el formulario.')
                password_form = CustomPasswordChangeForm(user=request.user)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = PerfilForm(instance=profile)
        password_form = CustomPasswordChangeForm(user=request.user)

    # Get fresh user data
    user = User.objects.get(pk=request.user.pk)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form,
        'profile': profile,
        'user': user  # Pass fresh user data to template
    }

    return render(request, 'adopcion/perfil.html', context)

def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('inicio')

def como_ayudar(request):
    return render(request, 'adopcion/como_ayudar.html')
