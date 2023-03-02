from .base import *
from sys import platform
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=BASE_DIR.parent / '.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("SECRET_KEY", None),
        'USER': os.getenv("DB_PRODUCTION_USER", None),
        'PASSWORD': os.getenv("DB_PRODUCTION_PASSWORD", None),
        'HOST': os.getenv("DB_PRODUCTION_HOST", None),
        'PORT': '',
    }
}

SECRET_KEY = os.getenv("SECRET_KEY", None)

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL='/static/'

STATIC_ROOT= BASE_DIR / 'static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media/'
