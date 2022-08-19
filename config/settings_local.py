DEBUG = True

SECRET_KEY = 'django-insecure-@3bx8!7tolzo@w5l8x2qufzwr#sca1^y50d*6r)!+e4&i#x0pp'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_pos_db',
        'USER': 'superusr',
        'PASSWORD': 5963,
        'HOST': 'db',
        'PORT': 5432,
    }
}
