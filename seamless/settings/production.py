from .base import *

if os.getenv('DATABASE_URL'):
    import django_heroku

    django_heroku.settings(locals())
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }
    DEBUG = False
    ALLOWED_HOSTS = ['localhost']
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
