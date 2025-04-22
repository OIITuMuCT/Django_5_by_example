from decouple import config
from .base import *

DEBUG = False
ADMINS = [
    ("admin", "admin@example.com"),
]
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
