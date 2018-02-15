DEBUG = False
ALLOWED_HOSTS = ['159.89.29.210',
                 'ekas-org.ru']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'ekas-group',
        'PASSWORD': 'echofoeadmin',
        'HOST': 'localhost',
        'PORT': '',

    }
}