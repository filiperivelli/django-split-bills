from os import environ

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'splitingbills.herokuapp.com',
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'splitbills',
        'HOST': 'localhost',
        'USER': environ['DB_USER'],
        'PASSWORD': environ['DB_PASSWORD'],
        'PORT':'5432',
    }
}