"""
WSGI config for django_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/root/django-api-env/lib/python3.6/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/root/django-api-env/lib/python3.6')

sys.path.append('/var/www/django-api-boilerplate')
sys.path.append('/var/www/django-api-boilerplate/django_api')

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_api.settings'

application = get_wsgi_application()
