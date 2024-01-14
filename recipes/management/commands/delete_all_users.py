from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Deletes all users in the database'

    def handle(self, *args, **options):
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all users'))