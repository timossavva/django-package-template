import os
import environ

from django.utils.translation import ugettext_lazy as _

env = environ.Env()
env.read_env('.env')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%ec(5!-$w1@p$c9hxx$kh4#brndur#0z%v8klxb#4t(hkud9c='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party
    #
    # Mine
    'core'
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'

# Database
# MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env('DB_NAME'),
#         'HOST': env('DB_HOST'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'PORT': env('DB_PORT'),
#     }
# }
# Or the default sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
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
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', _('English')),
    ('el', _('Greek')),
]
TIME_ZONE = 'Europe/Athens'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# --------------------------------------------------------- Static --------------------------------------------------- #
STATIC_URL = '/static/'
# The absolute path to the directory where ./manage.py collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# --------------------------------------------------------- Media ---------------------------------------------------- #
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# -------------------------------------------------------- Session --------------------------------------------------- #
# Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2

# ---------------------------------------------------- Login / Logout ------------------------------------------------ #
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'

# ---------------------------------------------------- Email Settings ------------------------------------------------ #
# Django email backend settings
# EMAIL_HOST = 'example.com'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'info@example.com'
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True
# ADMINS = [('Example', 'info@example.com')]

# ------------------------------------------------------- Logger ----------------------------------------------------- #
TEST_LOG_FILE_PATH = os.path.join(BASE_DIR, 'logs', 'test.dev')
# Create dirs if they not exist.
os.makedirs(os.path.dirname(TEST_LOG_FILE_PATH), exist_ok=True)
U_LOGFILE_SIZE = 5 * 1024 * 1024
U_LOGFILE_COUNT = 2
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
            'include_html': True,
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': TEST_LOG_FILE_PATH,
            'maxBytes': U_LOGFILE_SIZE,
            'backupCount': U_LOGFILE_COUNT,
            'encoding': 'utf8',  # this fixes UnicodeEncodeError
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        # Default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'test': {
            'handlers': ['file', 'console', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # You can log to the test logger using this function. This function will log the error to the `console`, to the
        # `file` and will send email with the error to the `mail_admins`.
        # log_message_to_logger(
        #     'error',
        #     'test',
        #     "We had an error while trying to execute...."
        #     "Error: {}".format(traceback.format_exc())
        # )
    },
}

# ----------------------------------------------- Django Specific Settings ------------------------------------------- #
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
# DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

# ---------------------------------------------------- Other Settings ------------------------------------------------ #
