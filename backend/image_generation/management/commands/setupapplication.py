from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    """Django command to execute custom management commands"""

    def handle(self, *args, **options):
        
        # Apply Migrations
        self.stdout.write('Applying migrations...')
        call_command('migrate', '--no-input')
        self.stdout.write(self.style.SUCCESS('Migrations complete!'))
        
        # # Insert Dummy Data
        self.stdout.write('Inserting dummy data...')
        call_command('insertdummydata')

        self.stdout.write(self.style.SUCCESS('Dummy Data inserted successfully!'))
        