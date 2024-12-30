from django.contrib.auth import get_user_model
import os
import django
from django.contrib.auth.hashers import make_password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mascota_rescate_core.settings')
django.setup()

User = get_user_model()

def fix_user(username='Juli0406', password='MascotaAdmin123!'):
    try:
        user = User.objects.get(username=username)
        print(f"\nUser found: {user.username}")
        print(f"Is superuser: {user.is_superuser}")
        print(f"Is staff: {user.is_staff}")
        print(f"Is active: {user.is_active}")
        
        # Make sure the user has all necessary permissions
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.password = make_password(password)
        user.save()
        
        print("\nUser updated successfully!")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print("Is active: True")
        print("Is staff: True")
        print("Is superuser: True")
            
    except User.DoesNotExist:
        # Create the user if it doesn't exist
        User.objects.create_superuser(
            username=username,
            email='admin@example.com',
            password=password
        )
        print(f"\nUser {username} created successfully!")
        print(f"Password: {password}")

if __name__ == '__main__':
    fix_user()
