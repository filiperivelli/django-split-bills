# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$)12c1ip+w@t8*_792ft@pmc$g95_2zrmlj$!52-xy-_z&&rwp'

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
        'USER': 'postgres',
        'PASSWORD': '123086',
        'PORT':'5432',
    }
}

django_heroku.settings(locals())