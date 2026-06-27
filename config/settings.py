"""
Django settings for config project.
"""

from pathlib import Path
import os
# pyrefly: ignore [missing-import]
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Безопасное получение ключа в прод, локально — фолбэк
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-j2&d(vq9de7kf$cag03cl*oqz)#!^4bzl$%uq@)qen(_)@y#h=')

# На Vercel по умолчанию False, локально можно задать через ENV
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['.vercel.app', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Идеально для Vercel
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

WSGI_APPLICATION = 'config.wsgi.application'


# --- АДАПТАЦИЯ ПОД SUPABASE & VERCEL ---
# Если в системе есть DATABASE_URL (на Vercel), парсим её с поддержкой SSL.
# Если переменной нет (локально), используем твою прямую строку подключения к Supabase Pooler.
SUPABASE_POOLER_URL = "postgresql://postgres.giomzfubnyrmjqnbkbpf:31190124dyus2011@aws-1-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require"

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', SUPABASE_POOLER_URL),
        conn_max_age=600,  # Удерживает соединение активным, ускоряя Serverless функции
        ssl_require=True   # Железное требование Supabase для пуллера
    )
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# --- НАСТРОЙКА СТАТИКИ (WHITENOISE) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_DIRS_PATH = os.path.join(BASE_DIR, 'static')
if os.path.exists(STATIC_DIRS_PATH):
    STATICFILES_DIRS = [STATIC_DIRS_PATH]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# --------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'api.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

CORS_ALLOW_ALL_ORIGINS = True