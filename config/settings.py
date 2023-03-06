"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static_local')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
##SECRET_KEY = 'django-insecure-xxxxxxxxxxxxxx12345'
SECRET_KEY: str | None = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
##DEBUG = True
##DEBUG = False
DEBUG: bool = os.getenv('DEBUG', 'False') == 'True'

##ALLOWED_HOSTS = ['*']
##ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else (os.getenv('ALLOWED_HOSTS').split(','))
ALLOWED_HOSTS: list[str] = os.getenv(
    'ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'django_cleanup',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'HOST': os.environ['DBHOST'],
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS']
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

##LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja'

##TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# ブラウザ上でアクセスするためのURLパス
##STATIC_URL = 'static/'
#STATIC_URL = 'ps/static/'
STATIC_URL = os.getenv('ENV_STATIC_URL')

FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

# ローカル環境で{% static %}タグを使った際に見に行く先のフォルダ
# collectstaticを実行した際に見に行くフォルダ
# CSSファイル等を読み込む先
STATICFILES_DIRS = [
    STATIC_DIR,
    os.path.join(FRONTEND_DIR, 'build', 'static')
]

STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')

# 集約用のパス
# 読み込んだファイルをまとめて出力する先
##STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_ROOT = os.path.join(BASE_DIR, 'ps/static')
STATIC_ROOT = os.path.join(BASE_DIR, os.getenv('ENV_STATIC_ROOT'))

#MEDIA_URL = '/ps/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'ps/media')

##MEDIA_URL = '/media/'
##MEDIA_URL = os.getenv('ENV_MEDIA_URL')
MEDIA_URL = os.getenv('ENV_MEDIA_URL', '/media/')
##MEDIA_ROOT = '/home/site/wwwroot/media'
##MEDIA_ROOT = os.getenv('ENV_MEDIA_ROOT')
##MEDIA_ROOT = (os.getenv('ENV_MEDIA_ROOT')) if 'ENV_MEDIA_ROOT' in os.getenv else (os.path.join(BASE_DIR, 'media'))
##MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = os.getenv('ENV_MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
##MEDIA_ROOT = os.environ('ENV_MEDIA_ROOT')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'app:login'
LOGIN_REDIRECT_URL = 'app:index'
LOGOUT_REDIRECT_URL = 'app:index' 

CSRF_TRUSTED_ORIGINS = ['https://tset-app-f1-django12345-docker.azurewebsites.net']

###CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
##CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else ['https://192.168.10.64']