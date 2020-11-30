from system.base_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# URL settings
ROOT_URLCONF = 'system.development.urls'

ALLOWED_HOSTS = ['127.0.0.1']

# Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

#Login Settings
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = "/accounts/logged_in/"
LOGOUT_REDIRECT_URL = "/accounts/login/"