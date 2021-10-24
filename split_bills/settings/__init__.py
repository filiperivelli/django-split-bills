from .base import *
import os
import django_heroku

if os.environ.get("ENV_NAME") == 'production':
    from .production import *
elif os.environ.get("ENV_NAME") == 'local':
    from .local import *
else:
    from .local import *

django_heroku.settings(locals())