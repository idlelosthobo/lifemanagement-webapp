from system.base_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# URL settings
ROOT_URLCONF = 'system.development.urls'

# Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'db',
        'PASSWORD': 'zbwwn9t0tysfo1pp',
        'HOST': 'app-d70a4f60-2f5d-41e9-9f67-2ed903d0c737-do-user-6683175-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

# Email Settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.office365.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'me@here.com'
# EMAIL_HOST_PASSWORD = 'me'
# DEFAULT_FROM_EMAIL = 'No Reply Address<noreply@here.com>'
# SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Static Settings
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

#Hosting Settings
WSGI_APPLICATION = 'system.development.wsgi.application'

