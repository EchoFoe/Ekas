DEBUG = False
ALLOWED_HOSTS = ['138.197.181.89',
                 'ekas-org.ru']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'ekas-group',
        'PASSWORD': 's',
        'HOST': 'localhost',
        'PORT': '',

    }
}
