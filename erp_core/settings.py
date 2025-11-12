import os
from pathlib import Path
from dotenv import load_dotenv

# =========================
# تحميل ملف البيئة (.env)
# =========================
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# مفاتيح الأمان والإعدادات
# =========================
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default")
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = ['shorofat-erp-system.onrender.com', '127.0.0.1', 'localhost']

ENV_MODE = os.getenv("ENV_MODE", "development")


# =========================
# التطبيقات المثبتة
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',

    # التطبيقات المحلية
    'accounts',
    'admin_dashboard',
    'employee_portal',
    'client_portal',
    'inventory',
    'hr',
    'sales',
    'projects',
    'clients',
]


# =========================
# Middleware
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================
# URLs / WSGI
# =========================
ROOT_URLCONF = 'erp_core.urls'
WSGI_APPLICATION = 'erp_core.wsgi.application'


# =========================
# Templates
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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


# =========================
# قواعد البيانات
# =========================
if ENV_MODE == "production":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# =========================
# المستخدم المخصص
# =========================
AUTH_USER_MODEL = 'accounts.User'


# =========================
# كلمات المرور
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =========================
# اللغة والتوقيت
# =========================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True


# =========================
# الملفات الثابتة
# =========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =========================
# تسجيل الدخول والخروج
# =========================
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = '/admin_dashboard/dashboard/'
LOGOUT_REDIRECT_URL = '/'


# =========================
# Django REST
# =========================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


# =========================
# إعدادات CORS
# =========================
CORS_ALLOW_ALL_ORIGINS = True


# =========================
# الإعداد الافتراضي للحقل الأساسي
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
