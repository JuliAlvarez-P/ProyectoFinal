from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _
from .models import Mascota, SolicitudAdopcion
from .forms import MascotaForm, SolicitudAdopcionForm

def inicio(request):
    """Vista de la página de inicio."""
    mascotas_recientes = Mascota.objects.all().order_by('-fecha_registro')[:6]
    return render(request, 'adopcion/inicio.html', {
        'mascotas_recientes': mascotas_recientes,
        'title': _('Inicio')
    })

def lista_mascotas(request):
    """Vista que muestra todas las mascotas disponibles."""
    mascotas = Mascota.objects.all().order_by('-fecha_registro')
    paginator = Paginator(mascotas, 9)  # 9 mascotas por página
    page = request.GET.get('page')
    mascotas = paginator.get_page(page)
    return render(request, 'adopcion/lista_mascotas.html', {
        'mascotas': mascotas,
        'title': _('Mascotas en Adopción')
    })

def detalle_mascota(request, mascota_id):
    """Vista que muestra el detalle de una mascota."""
    mascota = get_object_or_404(Mascota, id=mascota_id)
    return render(request, 'adopcion/detalle_mascota.html', {
        'mascota': mascota,
        'title': mascota.nombre
    })

@login_required
def publicar_mascota(request):
    """Vista para publicar una nueva mascota."""
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.usuario = request.user
            mascota.save()
            messages.success(request, _('Mascota publicada exitosamente'))
            return redirect('adopcion:lista_mascotas')
    else:
        form = MascotaForm()
    
    return render(request, 'adopcion/publicar_mascota.html', {
        'form': form,
        'title': _('Publicar Mascota')
    })

@login_required
def editar_mascota(request, pk):
    """Vista para editar una mascota existente."""
    mascota = get_object_or_404(Mascota, pk=pk)
    
    # Verificar que el usuario sea el dueño de la mascota
    if mascota.usuario != request.user:
        messages.error(request, _('No tienes permiso para editar esta mascota'))
        return redirect('adopcion:lista_mascotas')
    
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            messages.success(request, _('Mascota actualizada exitosamente'))
            return redirect('adopcion:detalle_mascota', mascota_id=mascota.id)
    else:
        form = MascotaForm(instance=mascota)
    
    return render(request, 'adopcion/editar_mascota.html', {
        'form': form,
        'mascota': mascota,
        'title': _('Editar Mascota')
    })

@login_required
def solicitar_adopcion(request, pk):
    """Vista para solicitar la adopción de una mascota."""
    mascota = get_object_or_404(Mascota, pk=pk)
    
    if request.method == 'POST':
        form = SolicitudAdopcionForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.mascota = mascota
            solicitud.usuario = request.user
            solicitud.save()
            messages.success(request, _('Solicitud enviada exitosamente'))
            return redirect('adopcion:detalle_mascota', mascota_id=mascota.id)
    else:
        form = SolicitudAdopcionForm()
    
    return render(request, 'adopcion/solicitar_adopcion.html', {
        'form': form,
        'mascota': mascota,
        'title': _('Solicitar Adopción')
    })

def como_ayudar(request):
    """Vista que muestra información sobre cómo ayudar."""
    return render(request, 'adopcion/como_ayudar.html', {
        'title': _('Cómo Ayudar')
    })

def como_ayudar(request):
    """Vista que muestra información sobre cómo ayudar."""
    return render(request, 'adopcion/como_ayudar.html', {
        'title': _('Cómo Ayudar')
    })
