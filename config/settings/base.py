"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
from decouple import config
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _ 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'apps.account.apps.AccountConfig',
    'apps.blog.apps.BlogConfig',
    'apps.like.apps.LikeConfig',
    'apps.comment.apps.CommentConfig',
    'apps.follow.apps.FollowConfig',
    'apps.activity.apps.ActivityConfig',
    'apps.newsletter.apps.NewsletterConfig',
]

THIRDPARTY_APPS = [
    # 'imagekit',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRDPARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', #intenationalization middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# CELERY SETTINGS
# CELERY_BROKER_URL = (
#     os.environ.get("CELERY_BROKER_URL", os.environ.get("CLOUDAMQP_URL")) or ""
# )
# CELERY_TASK_ALWAYS_EAGER = not CELERY_BROKER_URL
# CELERY_ACCEPT_CONTENT = ["json"]
# CELERY_TASK_SERIALIZER = "json"
# CELERY_RESULT_SERIALIZER = "json"
# CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", None)


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True 

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ("en", _("English")),
    ('es', _('Spanish')),
    ("fr", _("French")), 
]

 
LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# NOTE :  use Amazon s3 to setup and serve static and media files in production.
# & Django doesn’t serve files itself; it leaves that job to whichever Web server you choose.

STATIC_URL = '/static/'

MEDIA_URL = '/media/'


STATICFILES_DIRS = [os.path.join(BASE_DIR,'static_files','static')]

STATIC_ROOT = os.path.join(BASE_DIR,'static_files','static_cdn')

MEDIA_ROOT = os.path.join(BASE_DIR,'media') 


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]


DEFAULT_AVATAR_URL = 'dp/default.png'

# RANDOM_AVATAR_PATH = os.path.join(BASE_DIR,'static_files','static','images','avatars') using static
RANDOM_AVATAR_PATH = os.path.join(MEDIA_ROOT,'default_avatars') 


import math
AVATAR_UPLOAD_SIZE_LIMIT = math.ceil(1228.53515625)

AVATAR_DIMENSION_SIZES = (150,200,250)

#uploads requirements
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]
ALLOWED_MIME_TYPES = ["image/png", "image/jpg", "image/jpeg"]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = { # noqa: WPS407
    'version': 1,
    'disable_existing_loggers': False,
    'filters':{
        'require_debug_false':{
            '()':'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

