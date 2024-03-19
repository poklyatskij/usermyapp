"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
import os

SECRET_KEY = os.getenv('SECRET_KEY')

# SECRET_KEY = 'django-insecure-(i5oajmrw2kn4qbw5ssxwo#oe1*5)v9qs^(qeo(ruztb148knw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


ALLOWED_HOSTS = [
    '127.0.0.1',
    '192.168.0.106',
    'usermyapp.pythonanywhere.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'myapp2',
    'myapp5',
    'myapp6',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'usermyapp$default',
        'USER': 'usermyapp',
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': 'usermyapp.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET NAMES 'utf8mb4';SETsql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGGING = {
 'version': 1,
 'disable_existing_loggers': False,
 'formatters': {
     'simple': {
         'format': '%(levelname)s %(message)s'
     },
     'verbose': {
         'format': '{levelname} {asctime} {module} {procces} {thread} {message}',
         'style': '{',
     },
 },
 'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
        'formatter': 'verbose',
    },
    'file': {
        'class': 'logging.FileHandler',
        'filename': './log/django.log',
        'formatter': 'verbose',
    },
 },
 'loggers': {
    'django': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'myapp': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG',
        'propagate': True,
    },
 },
}