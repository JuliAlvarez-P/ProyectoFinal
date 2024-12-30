from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from .models import Message
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
@require_http_methods(["GET"])
def inbox(request):
    """Display user's inbox with received and sent messages."""
    context = {
        'messages_received': Message.objects.filter(receiver=request.user),
        'messages_sent': Message.objects.filter(sender=request.user),
        'title': 'Buzón de Mensajes'
    }
    return render(request, 'messaging/inbox.html', context)

@login_required
@require_http_methods(["GET", "POST"])
def send_message(request, receiver_id):
    """Handle sending messages to other users."""
    receiver = get_object_or_404(User, id=receiver_id)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                sender=request.user,
                receiver=receiver,
                content=content
            )
            messages.success(request, 'Mensaje enviado exitosamente')
            return redirect('inbox')
        else:
            messages.error(request, 'El mensaje no puede estar vacío')
    
    return render(request, 'messaging/send_message.html', {
        'receiver': receiver,
        'title': f'Enviar mensaje a {receiver.username}'
    })

@login_required
@require_http_methods(["GET"])
def view_message(request, message_id):
    """Display a specific message and mark it as read if necessary."""
    message = get_object_or_404(Message.objects.filter(
        Q(receiver=request.user) | Q(sender=request.user)
    ), id=message_id)
    
    if message.receiver == request.user and not message.is_read:
        message.mark_as_read()
    
    return render(request, 'messaging/view_message.html', {
        'message': message,
        'title': 'Ver Mensaje'
    })
