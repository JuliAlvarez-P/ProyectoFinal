from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm

def registro(request):
    """View for user registration."""
    if request.user.is_authenticated:
        return redirect('adopcion:inicio')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, _('¡Registro exitoso! Bienvenido a nuestra comunidad.'))
            return redirect('adopcion:inicio')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {
        'form': form,
        'title': _('Registro')
    })

@login_required
def perfil(request):
    """View for user profile management."""
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Tu perfil ha sido actualizado exitosamente.'))
            return redirect('accounts:perfil')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'accounts/profile.html', {
        'form': form,
        'title': _('Mi Perfil')
    })
