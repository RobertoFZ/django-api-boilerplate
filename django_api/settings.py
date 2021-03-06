"""
Django settings for django_api project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
from django.utils.translation import ugettext_lazy as _
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# We load the .env file
load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

URL_SERVER = os.getenv('URL_SERVER')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOST').split(',') if os.getenv('ALLOWED_HOST') != None else []

CORS_ORIGIN_ALLOW_ALL = True if str(os.getenv('CORS_ORIGIN_ALLOW_ALL')) in [
    'True', 'true', '1'] else False
CORS_ORIGIN_WHITELIST = os.getenv('CORS_ORIGIN_WHITELIST').split(',') if os.getenv('CORS_ORIGIN_WHITELIST') != None else []

CONTACT_EMAIL = os.getenv('CONTACT_EMAIL')

ONE_SIGNAL_APP_ID = os.getenv('ONE_SIGNAL_APP_ID')
ONE_SIGNAL_TOKEN = os.getenv('ONE_SIGNAL_TOKEN')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party apps
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
     # Own applications
    'django_api.api_v1'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': os.getenv('PAGE_SIZE')
}

ROOT_URLCONF = 'django_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME') if os.getenv('DB_NAME') != None else 'django_api',
        'USER': os.getenv('DB_USER') if os.getenv('DB_USER') != None else 'root',
        'PASSWORD': os.getenv('DB_PASSWORD') if os.getenv('DB_PASSWORD') != None else '',
        'HOST': os.getenv('DB_HOST') if os.getenv('DB_HOST') != None else 'localhost',
        'PORT': os.getenv('DB_PORT') if os.getenv('DB_PORT') != None else 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

ugettext = lambda s: s
LANGUAGES = (
    ('es', ugettext('Espa??ol')),
    ('en', ugettext('Ingl??s')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Merida'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_PATH = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    STATIC_PATH,
)
__STATIC_PATH = os.path.dirname(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(__STATIC_PATH, "../static") if str(os.getenv(
    'ENV')) == 'development' else os.path.join(__STATIC_PATH, "../../static")

STATIC_URL = '/static/'

#   MEDIA FILES

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email Section
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_DEFAULT_FROM')
SERVER_EMAIL = os.getenv('EMAIL_HOST_USER')
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_POST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_CONTACT_FROM = os.getenv('EMAIL_CONTACT_FROM')


# USER SECTION

AUTH_USER_MODEL = 'api_v1.User'
