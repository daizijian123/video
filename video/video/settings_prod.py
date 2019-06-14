from .settings import *

import pymysql

pymysql.install_as_MySQLdb()

MODE = 'nginx'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'video',
        'USER': 'root',
        'PASSWORD': 'Quattro!',
    }
}

STATIC_ROOT = '/var/video/static/'
MEDIA_ROOT = '/var/video/media/'
