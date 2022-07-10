"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os

from dotenv import load_dotenv
GITPOD_ENV_FILE = "./gitpod_insecure.env"
DEFAULT_ENV_FILE = "./.env"

on_gitpod = os.getenv("GITPOD_WORKSPACE_CONTEXT", False)
dot_env_file = GITPOD_ENV_FILE if on_gitpod else DEFAULT_ENV_FILE


load_dotenv(dotenv_path=dot_env_file, interpolate=False)

postgres_port = os.getenv("POSTGRES_PORT")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_user = os.getenv("POSTGRES_USER")
postgres_database = os.getenv("POSTGRES_DATABASE")
postgres_host = os.getenv("POSTGRES_HOST")
django_secret_key = os.getenv("DJANGO_SECRET_KEY")
debug_mode = os.getenv("DEBUG_MODE")

if (not postgres_host) or (not postgres_password) or (not postgres_user):
    raise RuntimeError("Missing required values.  Looking for environment variables. like POSTGRES_USER. "
                       f"check the beinging of {__file__} and figure out what is wrong."
                       "\nIf you copied this from github to run locally, probably you need to create an "
                       ".env file with secres in the same directory as manage.py.  The format should "
                       "be in gitpod_insecure.env in that folder, change the configs for your local postgres.")

# If you want to change this to your own settings see
# https://www.gitpod.io/guides/automate-env-files-with-gitpod-environment-variables

DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap.html"

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = django_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.localhost', '.gitpod.io']


# Application definition


INSTALLED_APPS = [
    'demos.apps.DemosAppConfig',
    'countries.apps.CountriesAppConfig',
    'django_tables2',
    'bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': postgres_database,
        'USER': postgres_user,
        'PASSWORD': postgres_password,
        'HOST': postgres_host,
        'PORT': postgres_port,
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
