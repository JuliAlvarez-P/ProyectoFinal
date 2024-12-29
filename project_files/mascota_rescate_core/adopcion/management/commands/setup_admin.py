from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Sets up juli0406 as admin and removes other users'

    def handle(self, *args, **options):
        # Remove all users except juli0406
        User.objects.exclude(username='juli0406').delete()
        
        # Create or update juli0406
        user, created = User.objects.get_or_create(username='juli0406')
        user.set_password('Pino040606')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created superuser juli0406'))
        else:
            self.stdout.write(self.style.SUCCESS('Updated superuser juli0406'))
        
        self.stdout.write(self.style.SUCCESS('Removed all other users'))
