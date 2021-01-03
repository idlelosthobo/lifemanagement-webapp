from system.base_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# URL settings
ROOT_URLCONF = 'system.production.urls'

# Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'development_dandy_organizer',
        'USER': 'dandyaccess',
        'PASSWORD': 'zv6l76rc8cp39d39',
        'HOST': 'db-mysql-tor1-30973-do-user-6683175-0.db.ondigitalocean.com',
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
WSGI_APPLICATION = 'system.production.wsgi.application'

