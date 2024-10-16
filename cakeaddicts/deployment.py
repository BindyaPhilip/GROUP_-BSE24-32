import os
from .settings import *
from .settings import BASE_DIR


SECRET_KEY = os.environ['SECRET']
#Only the URL created by Azure will be allowed
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']

#parameters = {pair.split('='):pair.split('=')[1] for pair in connection_string.split(' ')}
parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : parameters['dbname'],
        'HOST' : parameters['host'],
        'USER' : parameters['user'],
        'PASSWORD' : parameters['password'],
        'PORT': parameters['port'],         # 5432
        'OPTIONS': {
            'sslmode': parameters['sslmode'], # require SSL
        },
        
        
        
        }

}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'azure': {
            'class': 'path.to.AzureLogHandler',  # Implement Azure Log handler
        },
    },
    'root': {
        'handlers': ['console', 'azure'],
        'level': 'WARNING',
    },
}
