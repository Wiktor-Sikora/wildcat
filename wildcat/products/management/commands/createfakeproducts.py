from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings
import sys
import json
import random

from products.models import Product

User = get_user_model()

def get_random_user():
    allowed_users = ('Tony_M_Goulding', 'Dorothy_E_Arndt', 'Paige_F_Caba', 'Drathe76')
    username = random.choice(allowed_users)
    return User.objects.get(username=username)

class Command(BaseCommand):
    help = 'Create fake products, run after createfakeusers command'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str, 
            default=settings.BASE_DIR / 'common/products-texts.json', 
            help='Force command execution when DEBUG = False')
        parser.add_argument('-r', '--force', action='store_true', default=False, help='Force command execution when DEBUG = False')

    def handle(self, *args, **options):
        if not settings.DEBUG and not options['force']:
            self.stdout.write(self.style.ERROR('Django is not running in DEBUG mode. Aborting'))
            sys.exit()

        self.stdout.write(self.style.MIGRATE_HEADING('Creating fake products'))
        with open(options['file']) as json_file:
            parsed_json = json.load(json_file)
        
        

        for product in parsed_json:
            Product.objects.create(name=product['name'], description=product['description'], owner=get_random_user())
            self.stdout.write(self.style.HTTP_INFO(f'Product {product["name"]} created'))
        self.stdout.write(self.style.SUCCESS(f'Succesfully created fake products'))
            