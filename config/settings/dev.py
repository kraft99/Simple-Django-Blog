from .base import *

DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS',
						cast=lambda x:[s.strip() for s in x.split(',')],
						default='127.0.0.1,localhost')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
