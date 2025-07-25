"""
Django settings for raadaa project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'insecure-key-for-dev-only')
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'
MAIN_DOMAIN = os.getenv('MAIN_DOMAIN', 'http://localhost:8000')
# ALLOWED_HOSTS configuration
# If DJANGO_ALLOWED_HOSTS is a comma-separated string in .env, split it into a list
allowed_hosts_str = os.getenv('DJANGO_ALLOWED_HOSTS')
ALLOWED_HOSTS = (
    allowed_hosts_str.split(',') if allowed_hosts_str
    else [
        MAIN_DOMAIN,
        '.' + MAIN_DOMAIN,
        'raadaa.onrender.com',
        'www.raadaa.onrender.com',
        'localhost',
        '*.localhost',
        '.localhost',
        '127.0.0.1',
        '.teammanager.ng',
        'teammanager.ng',
        'transnet-cloud.localhost',
        'raadaa.localhost',
        'miniago.localhost',
        '13.61.189.68',  # Add test host IP
    ]
)

# CSRF_TRUSTED_ORIGINS configuration
# If CSRF_TRUSTED_ORIGINS is a comma-separated string in .env, split it into a list
csrf_trusted_origins_str = os.getenv('CSRF_TRUSTED_ORIGINS')
CSRF_TRUSTED_ORIGINS = (
    csrf_trusted_origins_str.split(',') if csrf_trusted_origins_str
    else [
        'https://teammanager.ng',
        'https://.teammanager.ng',
        'https://raadaa.onrender.com',
        'https://*.onrender.com',
        'http://localhost:8000',
        'http://*.localhost:8000',
        'http://.localhost:8000',
        'http://127.0.0.1:8000',
        'http://transnet-cloud.localhost:8000',
        'http://raadaa.localhost:8000',
        'http://miniago.localhost:8000',
        'http://13.61.189.68:8000',  # Add test host IP
    ]
)

# Temporarily disable CSRF_COOKIE_SECURE for HTTP testing
CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE', 'False') == 'True'
SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'False') == 'True'
SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'False') == 'True'  # Redirect HTTP to HTTPS
# CSRF_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = False
# SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

LOGIN_REDIRECT_URL = "home"  # Redirect to dashboard after login
LOGOUT_REDIRECT_URL = "login"  # Redirect to login after logout
# PDFKIT_CONFIG = {
#     'wkhtmltopdf': r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
# }
AUTH_USER_MODEL = "documents.CustomUser"

# Zoho email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.zoho.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

X_FRAME_OPTIONS = 'SAMEORIGIN'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "DEBUG" if DEBUG else "INFO",
        },
    },
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-e0nt-wx^4!^!r1#rn!*g@6@!bp%q=j2m94o8s105%5+ctbzf*0'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'documents.apps.DocumentsConfig',
    'tenants',
    'ckeditor',
    'ckeditor_uploader',
    'django_cron',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tenants.middleware.TenantMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'raadaa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "documents/templates")],
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

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'documents.context_processors.notification_bar',
    'documents.context_processors.notification_count',
]

WSGI_APPLICATION = 'raadaa.wsgi.application'

CRON_CLASSES = [
    "documents.cron.BirthdayNotificationCronJob",
    "documents.cron.EventReminderCronJob",
]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Database
if os.getenv("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv("DATABASE_URL"),
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# CKEditor upload path
CKEDITOR_UPLOAD_PATH = "Uploads/"
# CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
    },
    'custom_toolbar': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat'],
            ['FontSize', 'Font', 'TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
            ['Link', 'Unlink', 'Image', 'Embed'],
            ['Format', 'Styles'],
            ['Source']
        ],
        'height': 400,
        'width': 'auto',
        'extraPlugins': ','.join([
            'uploadimage',  # upload images
            'embed',        # media embeds
            'autoembed',
        ]),
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'removePlugins': 'stylesheetparser',
    },
}

CKEDITOR_RESTRICT_BY_USER = False  # Allow all users to upload


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
