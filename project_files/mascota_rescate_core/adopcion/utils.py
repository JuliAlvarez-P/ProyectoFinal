"""Utility functions for the adopcion app."""
from django.core.exceptions import PermissionDenied
from functools import wraps

def admin_required(view_func):
    """Decorator to require admin access for views."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def handle_uploaded_image(image, path):
    """Handle image upload with proper error handling."""
    try:
        with open(path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        return True
    except Exception:
        return False
