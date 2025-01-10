from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        self.execute_all()

    def execute_all(self):
        self.create_super_user()
        
    def create_super_user(self):
        self.stdout.write('Creating superuser')

        email = "admin@example.com"
        password = "admin@123"
        first_name = 'admin'
        last_name = 'admin'
        username = 'admin'

        try:
            if User.objects.filter(email=email).exists():
                self.stdout.write(self.style.WARNING('Superuser already exists: {}'.format(email)))
                return
            user = User.objects.create_superuser(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                username=username
            )

            self.stdout.write(self.style.SUCCESS('Superuser created successfully: {}'.format(user)))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error creating superuser: {}'.format(str(e))))
      