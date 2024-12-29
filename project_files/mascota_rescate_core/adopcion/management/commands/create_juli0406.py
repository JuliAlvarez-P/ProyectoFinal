from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates the Juli0406 superuser account'

    def handle(self, *args, **options):
        if User.objects.filter(username='Juli0406').exists():
            User.objects.filter(username='Juli0406').delete()
            self.stdout.write('Deleted existing Juli0406 account')
        
        user = User.objects.create_superuser(
            username='Juli0406',
            password='Pino040606',
            email='Juli0406@example.com'
        )
        self.stdout.write(self.style.SUCCESS('Successfully created Juli0406 superuser'))
