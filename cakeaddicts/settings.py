"""
Django settings for cakeaddicts project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from decouple import config
import pymysql



pymysql.install_as_MySQLdb()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-b0%zs_fyk!@-d03w782n+dt5y)*k!bfb!=s7g36m)823yzq%(+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'cakestore.apps.CakestoreConfig',
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

ROOT_URLCONF = 'cakeaddicts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'cakeaddicts.wsgi.application'

IS_STAGING = os.getenv('IS_STAGING', 'False') == 'True'

if not IS_STAGING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('MYSQL_DATABASE_NAME'),
            'USER': os.getenv('MYSQL_DATABASE_USER'),
            'PASSWORD': os.getenv('MYSQL_DATABASE_PASSWORD'),
            #'HOST': os.getenv('MYSQL_DATABASE_HOST'),  # Usually something like 'localhost' or the remote DB host
            'PORT': os.getenv('MYSQL_DATABASE_PORT', '3306'),  # MySQL typically runs on port 3306
        }
    }





# Determine the environment
#ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')  # defaults to 'development'

#if ENVIRONMENT == 'development':
    # Use SQLite for development
 #   DATABASES = {
  #      'default': {
  #          'ENGINE': 'django.db.backends.sqlite3',
  #          'NAME': BASE_DIR / "db.sqlite3",
   #     }
    #}
#else:
    # Use MySQL for staging/production
 #   DATABASES = {
  #      'default': {
   #         'ENGINE': 'django.db.backends.mysql',
    #        'NAME': os.getenv('MYSQL_DB_NAME', 'production_db'),
     #       'USER': os.getenv('MYSQL_DB_USER', 'myusername'),
      #      'PASSWORD': os.getenv('MYSQL_DB_PASSWORD', 'mypassword'),
       #     'HOST': os.getenv('MYSQL_DB_HOST', 'mystagingdb.mysql.database.azure.com'),
        #    'PORT': '3306',
       # }
   # }
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': BASE_DIR / 'db.sqlite3',
   # }
#}
#IS_STAGING = os.getenv('IS_STAGING', 'False') == 'True'

#if not IS_STAGING:
    # Development: Use SQLite
 #   DATABASES = {
  #      'default': {
   #         'ENGINE': 'django.db.backends.sqlite3',
    #        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      #  }
   # }
#else:
    # Staging/Production: Use PostgreSQL/MySQL
 #   DATABASES = {
  #      'default': dj_database_url.config(
   #         default=os.getenv('DATABASE_URL')
    #    )
    #}

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

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = 'uploadMedia/'
# MEDIA_ROOT =  os.path.join(BASE_DIR, '/media/images') 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/images')
STATICFILES_DIRS = [
    BASE_DIR / "static",  # This is the general static folder at the base level
    os.path.join(BASE_DIR, 'cakestore', 'static'),  # This points to the static folder within the cakestore app
]

#STATICFILES_DIRS = ( 
#    'cakestore',
    # os.path.join(BASE_DIR, 'static'),
 #   )


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#keys for the stripe api (payment gateway)
#STRIPE_SECRET_KEY = 'sk_test_51LmstwIcrvW4NoX9f0FtWODlbP8XiuRtd6817oFqFa1cYvWbUZNYhrveRxCExIwzJunj3lts9uVjbm7Rm7rRUY7P002PoVLWMe'
#STRIPE_PUBLISHABLE_KEY = 'pk_test_51LmstwIcrvW4NoX9WGPDv6PZ52lt8oc3vq9e5ynZ3bg2EU2djQVLWM64GYsWGYOpTwKk7SCMO9ZpwdDj0UkqpXEx00KLuwwyEd'
SECRET_KEY = config('SECRET_KEY')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
#HEROKU_API_KEY = config('HEROKU_API_KEY')


#STMP CONFIG
from django.core.mail import send_mail
EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'rujumbaleonard2@gmail.com'
#EMAIL_HOST_PASSWORD = 'ihkxvuxwwgmardib'