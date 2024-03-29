"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from os import getcwd, mkdir,path,getenv,listdir
from glob import iglob
from dotenv import load_dotenv
from socket import gethostbyname,gethostname

IP_ADDRESS=gethostbyname(gethostname())
load_dotenv()
FILE=getcwd()
NAME_OF_FOLDER_CONTAINING_MANAGE_PY_FILE="dd_pay2"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY= getenv("SECRET_KEY")

SECRET_KEY=SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["102.22.14.198"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend'
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

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        #"NAME":list([DATABASE_FILE for idx,DATABASE_FILE in enumerate((iglob(f"{FILE}/{NAME_OF_FOLDER_CONTAINING_MANAGE_PY_FILE}/**/db.sqlite3",recursive=True)))])[0]  if "db.sqlite3" in list(listdir(f"{FILE}/{NAME_OF_FOLDER_CONTAINING_MANAGE_PY_FILE}")) else f"{FILE}/{NAME_OF_FOLDER_CONTAINING_MANAGE_PY_FILE}/db.sqlite3",
        "NAME":"/var/www/html/dd_pay2/db.sqlite3"
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

for idx,data in enumerate((iglob(f"{FILE}/{NAME_OF_FOLDER_CONTAINING_MANAGE_PY_FILE}/**/static",recursive=True))):
    PATH_TO_STATIC_FOLDER=data
    PATH_TO_MEDIA_FOLDER=data.replace("static","media")
    STATIC_ROOT=PATH_TO_STATIC_FOLDER
    try:
        mkdir(PATH_TO_MEDIA_FOLDER)
    except FileExistsError:
        ...
    MEDIA_ROOT=PATH_TO_MEDIA_FOLDER

STATIC_URL = 'static/'
MEDIA_URL="/media/"




# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#SESSION_COOKIE_SECURE=True
#CSRF_COOKIE_SECURE=True
#CONN_MAX_AGE=0
#CONN_HEALTH_CHECKS=True
