#db_setting.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lmr_db',
        'USER': 'lmr',
        'PASSWORD': 'lmr',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
