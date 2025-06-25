from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-_pt^@rm4)((^9=oi%3*e)mf7o%x9!12&1sr@vh4n6lq&3zg@$8'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'jazzmin',

    'django_light',

    'admin_tools_stats',  # this must be BEFORE 'admin_tools' and 'django.contrib.admin'
    'django_nvd3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_ckeditor_5',
    'django.contrib.staticfiles',
    'accounts',
    'pages',
    'news',
    'comments',
    'crispy_forms',

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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,  # Kamida 6 belgidan iborat parol talab qilinadi
        }
    },
]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Authentication
AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# CKEditor 5 configuration
customColorPalette = [
    {'color': 'hsl(4, 90%, 58%)', 'label': 'Red'},
    {'color': 'hsl(340, 82%, 52%)', 'label': 'Pink'},
    {'color': 'hsl(291, 64%, 42%)', 'label': 'Purple'},
    {'color': 'hsl(262, 52%, 47%)', 'label': 'Deep Purple'},
    {'color': 'hsl(231, 48%, 48%)', 'label': 'Indigo'},
    {'color': 'hsl(207, 90%, 54%)', 'label': 'Blue'},
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': [
                'heading', '|', 'bold', 'italic', 'link',
                'bulletedList', 'numberedList', 'blockQuote', 'imageUpload',
            ]
        },
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': {
            'items': [
                'heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline',
                'strikethrough', 'code', 'subscript', 'superscript', 'highlight', '|',
                'codeBlock', 'sourceEditing', 'insertImage', 'bulletedList', 'numberedList',
                'todoList', '|', 'blockQuote', 'imageUpload', '|', 'fontSize', 'fontFamily',
                'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat', 'insertTable',
            ],
            'shouldNotGroupWhenFull': True
        },
        'image': {
            'toolbar': [
                'imageTextAlternative', '|', 'imageStyle:alignLeft',
                'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side', '|'
            ],
            'styles': [
                'full', 'side', 'alignLeft', 'alignRight', 'alignCenter',
            ]
        },
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells',
                'tableProperties', 'tableCellProperties'
            ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'}
            ]
        }
    }
}

CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# settings.py
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Bu o'zgaruvchi loyiha papkangizdagi staticfiles papkasini ko'rsatishi kerak

JAZZMIN_SETTINGS = {
    "site_title": "PecDev Admin",
    "site_header": "PecDev",
    "site_brand": "PecDev",

    # Path should be relative to static directory, e.g. "img/logo.png"
    "site_logo": "img/logo.png",
    "login_logo": "img/logo.png",
    "login_logo_dark": "img/logo.png",  # For dark theme, use a logo with light colors if available
    "site_logo_classes": "img-circle",
    "site_icon": "img/favicon.ico",

    "welcome_sign": "Welcome to the library",
    "copyright": "Acme Library Ltd",

    "search_model": ["auth.User", "auth.Group"],
    "user_avatar": None,

    # THEME SETTINGS: Allow user to switch between light and dark
    # See: https://django-jazzmin.readthedocs.io/en/latest/themes/
    # Possible values: "default", "darkly", "cerulean", "cosmo", "cyborg", "flatly", "journal", "litera", "lumen", "lux", "materia", "minty", "pulse", "sandstone", "simplex", "sketchy", "slate", "solar", "spacelab", "superhero", "united", "yeti"

    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.User"},
        # {"app": "books"},  # Uncomment if 'books' app exists
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth"],  # Add your apps/models as needed

    "custom_links": {
        # Example for custom app links
        # "books": [{
        #     "name": "Make Messages",
        #     "url": "make_messages",
        #     "icon": "fas fa-comments",
        #     "permissions": ["books.view_book"]
        # }]
    },

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": False,

    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    "changeform_format": "carousel",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "language_chooser": True,
}
JAZZMIN_UI_TWEAKS = {

    "theme": "slate",
}