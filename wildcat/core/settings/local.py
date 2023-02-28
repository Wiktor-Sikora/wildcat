from .base import *
from sys import platform
from dotenv import load_dotenv

SECRET_KEY = 'l(3yoq9#6i04+6=4jw9u30+ex-o_3-xjf!medrg26zww##9az#l(3yoq9#6i04+6=4jw9u30+ex-o_3-xjf!medrg26zww##9az#'

DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS=["http://localhost:8000", "https://*.app.github.dev"]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media/'

if platform == 'win32':
    NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

load_dotenv(dotenv_path=BASE_DIR.parent / '.env')