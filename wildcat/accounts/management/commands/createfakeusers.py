from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.models import Product
from django.conf import settings
import sys
import json

User = get_user_model()

class Command(BaseCommand):
    help = 'Create fake users'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str, 
            default=settings.BASE_DIR / 'common/users-texts.json', 
            help='Force command execution when DEBUG = False')
        parser.add_argument('-r', '--force', action='store_true', default=False, help='Force command execution when DEBUG = False')

    def handle(self, *args, **options):
        if not settings.DEBUG and not options['force']:
            self.stdout.write(self.style.ERROR('Django is not running in DEBUG mode. Aborting'))
            sys.exit()

        self.stdout.write(self.style.MIGRATE_HEADING('Creating fake users'))
        with open(options['file']) as json_file:
            parsed_json = json.load(json_file)
        
        for user in parsed_json:
            User.objects.create(username=user['username'], email=user['email'], password=user['password'])
            self.stdout.write(self.style.HTTP_INFO(f'User {user["username"]} created'))
        self.stdout.write(self.style.SUCCESS(f'Succesfully created fake users'))
            