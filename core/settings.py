import os
from django.urls import reverse_lazy
from pathlib import Path
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition
INSTALLED_APPS = [
    'unfold',
    "unfold.contrib.filters",
    "unfold.contrib.inlines",
    "unfold.contrib.forms",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ### My Apps ###
    'main',
    'menu',
    'contact',
    'extra',

    ### 3rd Party Apps ###
    'tinymce',
    'mptt',
    'django_mptt_admin',

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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

CSRF_TRUSTED_ORIGINS = [
    "https://mybonusreward.ru",
    "https://www.mybonusreward.ru",
]


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3')
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]
 
STATIC_ROOT = '/home/batumibo/bonus.lumos.com.ge/static/'
MEDIA_ROOT = '/home/batumibo/bonus.lumos.com.ge/media/'
MEDIA_URL = '/media/'


# MEDIA_ROOT = os.path.join(BASE_DIR / "media")
# MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



UNFOLD = {
    "SITE_TITLE": "Administration Page",
    "SITE_HEADER": "My Bonus Reward",
    "SITE_SUBHEADER": "Administration page",
    "SIDEBAR": {
        "show_search": True,
        "navigation": [
            {
                "title": "Контейнеры",
                "icon": "location_on",
                "collapsible": True,
                "items": [
                    {
                        "title": "Главный контейнер",
                        "link": reverse_lazy("admin:main_firstcontainer_changelist"),
                    },
                    {
                        "title": "Второй контейнер",
                        "link": reverse_lazy("admin:main_secondcontainer_changelist"),
                    },
                    {
                        "title": "Третий контейнер",
                        "link": reverse_lazy("admin:main_thirdcontainer_changelist"),
                    },
                    {
                        "title": "Четвертый контейнер",
                        "link": reverse_lazy("admin:main_fourthcontainer_changelist"),
                    },
                    {
                        "title": "Пятый контейнер",
                        "link": reverse_lazy("admin:main_fivethcontainer_changelist"),
                    },
                    {
                        "title": "Шестой контейнер",
                        "link": reverse_lazy("admin:main_sixthcontainer_changelist"),
                    },
                    {
                        "title": "Седьмой контейнер",
                        "link": reverse_lazy("admin:main_seventhcontainer_changelist"),
                    },
                    {
                        "title": "Восьмой контейнер",
                        "link": reverse_lazy("admin:main_eighthcontainer_changelist"),
                    },
                    {
                        "title": "Девятый контейнер",
                        "link": reverse_lazy("admin:main_ninthcontainer_changelist"),
                    },
                    {
                        "title": "Десятый контейнер",
                        "link": reverse_lazy("admin:main_tenthcontainer_changelist"),
                    },
                    
                ],
            },
            {
                "title": "Меню",
                "icon": "settings",
                "collapsible": True,
                "items": [
                    {
                        "title": "Главное меню",
                        "link": reverse_lazy("admin:menu_menuitem_changelist"),
                    },
                    {
                        "title": "Нижнее меню",
                        "link": reverse_lazy("admin:menu_footermenu_changelist"),
                    },
                ],
            },
            {
                "title": "Сообщения",
                "icon": "settings",
                "collapsible": True,
                "items": [
                    {
                        "title": "Сообщения",
                        "link": reverse_lazy("admin:contact_contact_changelist"),
                    },
                ],
            },
            {
                "title": "Дополнительные настройки",
                "icon": "settings",
                "collapsible": True,
                "items": [
                    {
                        "title": "Условия использования",
                        "link": reverse_lazy("admin:extra_terms_changelist"),
                    },
                    {
                        "title": "Логотип",
                        "link": reverse_lazy("admin:extra_logo_changelist"),
                    },
                    {
                        "title": "Фавикон",
                        "link": reverse_lazy("admin:extra_favicon_changelist"),
                    },
                    {
                        "title": "Аналитика",
                        "link": reverse_lazy("admin:extra_analytics_changelist"),
                    },
                ],
            },
        ],
    }
}



TINYMCE_DEFAULT_CONFIG = {
    'height': 260,
    'width': '100%',
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    'font_formats': (
        'Andale Mono=andale mono,times;'
        'Arial=arial,helvetica,sans-serif;'
        'Arial Black=arial black,avant garde;'
        'Book Antiqua=book antiqua,palatino;'
        'Comic Sans MS=comic sans ms,sans-serif;'
        'Courier New=courier new,courier;'
        'Georgia=georgia,palatino;'
        'Helvetica=helvetica;'
        'Impact=impact,chicago;'
        'Open Sans=open sans,sans-serif;'
        'Roboto=roboto,sans-serif;'
        'Times New Roman=times new roman,times;'
        'Verdana=verdana,geneva;'
    ),
    "custom_undo_redo_levels": 20,
    "language": "ru-RU",  # To force a specific language instead of the Django current language.
}