from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=kb_t$-$=w006hviq!_n%brvoncjk$%lw2@^@zd*8bk36*z_$l'

INTERNAL_IPS = (
    '127.0.0.1',
)

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
]

INSTALLED_APPS += [
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'webpush',
    'pwa',
]

INSTALLED_APPS += [
    'app.comment.apps.CommentConfig',
    'app.core.apps.CoreConfig',
    'app.event.apps.EventConfig',
    'app.finance.apps.FinanceConfig',
    'app.group.apps.GroupConfig',
    'app.invitation.apps.InvitationConfig',
    'app.list.apps.ListConfig',
    'app.note.apps.NoteConfig',
    'app.people.apps.PeopleConfig',
    'app.registration.apps.RegistrationConfig',
    'app.subject.apps.SubjectConfig',
    'app.task.apps.TaskConfig',
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

ROOT_URLCONF = 'system.base_urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.core.context_processors.software_information',
            ],
        },
    },
]

# Allauth Settings

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

WEBPUSH_SETTINGS = {
    'VAPID_PUBLIC_KEY': 'BFEnTPYe0Ur1NAdUkR0S6dXch7_qVK8Fj6HJyXQF6Zd8DTRReZdRQ814sa2KbapffhlLWZZMEq4AiELpiWL3Yfc',
    'VAPID_PRIVATE_KEY': 'HAG02n_DS9dWZsoHhZI1oHUn26bVrVWRezAvdXsKONQ',
    'VAPID_ADMIN_EMAIL': 'drugen@gmail.com'
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login Settings

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'welcome'
LOGOUT_REDIRECT_URL = 'account_login'

# PWA Settings

PWA_APP_NAME = 'Dandy Organizer'
PWA_APP_DESCRIPTION = "An organizer to manage everything in your life"
PWA_APP_THEME_COLOR = '#ffffff'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/app/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/app/accounts/login/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/core/img/favicons/dandy-organizer-192.png',
        'sizes': '192x192'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/core/img/favicons/dandy-organizer-192.png',
        'sizes': '192x192'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'