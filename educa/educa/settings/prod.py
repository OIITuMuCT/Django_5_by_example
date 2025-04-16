from .base import *

DEBUG = False

ADMINS = [
    ('Admin', 'admin@example.com'),

]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backend.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
