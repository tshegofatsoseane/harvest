# accounts/management/commands/create_profiles.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.accounts.models import Profile

class Command(BaseCommand):
    help = 'Create profiles for users without one'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            Profile.objects.get_or_create(user=user)
        self.stdout.write(self.style.SUCCESS('Successfully created profiles for all users'))
