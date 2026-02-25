from .base import *
import environ 
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

DEBUG = False

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'HOST': env('DATABASE_HOST'),
        'PORT': 5432,
		    'USER': env('DATABASE_USER'),
		    'PASSWORD': env('DATABASE_PASS'),
        'TEST': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('DATABASE_NAME'),
            'HOST': env('DATABASE_HOST'),
            'PORT': 5432,
            'USER': env('DATABASE_USER'),
            'PASSWORD': env('DATABASE_PASS'),
        }
    },
}
