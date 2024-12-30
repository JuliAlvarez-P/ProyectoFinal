from django.contrib.auth import get_user_model
import os
import django
from django.contrib.auth.hashers import make_password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mascota_rescate_core.settings')
django.setup()

User = get_user_model()

def verify_and_fix_user(username):
    try:
        user = User.objects.get(username=username)
        print(f"\nUser found: {user.username}")
        print(f"Is superuser: {user.is_superuser}")
        print(f"Is staff: {user.is_staff}")
        print(f"Is active: {user.is_active}")
        
        # Make sure the user is active and staff
        if not user.is_active or not user.is_staff:
            user.is_active = True
            user.is_staff = True
            user.save()
            print("\nFixed user permissions:")
            print(f"Is active: {user.is_active}")
            print(f"Is staff: {user.is_staff}")
        
        # Option to reset password
        reset = input("\nWould you like to reset the password? (yes/no): ")
        if reset.lower() == 'yes':
            new_password = input("Enter new password: ")
            user.password = make_password(new_password)
            user.save()
            print("Password has been reset successfully!")
            
    except User.DoesNotExist:
        print(f"\nUser {username} not found!")
        create = input("Would you like to create this user? (yes/no): ")
        if create.lower() == 'yes':
            password = input("Enter password for new user: ")
            User.objects.create_user(
                username=username,
                password=password,
                is_staff=True,
                is_active=True
            )
            print(f"\nUser {username} created successfully!")

if __name__ == '__main__':
    username = input("Enter username to verify: ")
    verify_and_fix_user(username)
