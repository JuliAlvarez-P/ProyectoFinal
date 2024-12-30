from django.contrib.auth import get_user_model
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mascota_rescate_core.settings')
django.setup()

User = get_user_model()

# Get the user and make them a superuser
try:
    user = User.objects.get(username='Juli0406')
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print(f"Successfully made {user.username} a superuser!")
except User.DoesNotExist:
    print("User Juli0406 not found")
