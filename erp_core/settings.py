"""
Django settings for ERP_SYSTEM project
"""

from pathlib import Path
import os

# =========================
# المسارات الأساسية
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# مفاتيح الأمان
# =========================
SECRET_KEY = 'django-insecure-change-this-in-production'
DEBUG = True
ALLOWED_HOSTS = ['*']


# =========================
# التطبيقات المثبتة
# =========================
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # مكتبات خارجية
    'corsheaders',
    'rest_framework',

    # تطبيقات النظام المحلية
    'accounts',           # المستخدمين وتسجيل الدخول
    'admin_dashboard',    # لوحة تحكم المدير
    'employee_portal',    # بوابة الموظف
    'client_portal',      # بوابة العميل
    'inventory',          # المخزون والمنتجات
    'hr',                 # الموارد البشرية والرواتب
    'sales',              # المبيعات والعمولات
    'projects',           # المشاريع والمهام
    'clients',            # العملاء والفواتير
]


# =========================
# الطبقات الوسيطة (Middleware)
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
# إعدادات الـ URLs و WSGI
# =========================
ROOT_URLCONF = 'erp_core.urls'
WSGI_APPLICATION = 'erp_core.wsgi.application'


# =========================
# إعدادات القوالب (Templates)
# =========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
# قاعدة البيانات (SQLite افتراضية - تطوير)
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # للإنتاج: استبدل بـ PostgreSQL أو MySQL
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'erp_db',
    #     'USER': 'erp_user',
    #     'PASSWORD': 'secure_password',
    #     'HOST': 'localhost',
    #     'PORT': '5432',
    # }
}


# =========================
# نموذج المستخدم المخصص
# =========================
AUTH_USER_MODEL = 'accounts.User'


# =========================
# إعدادات كلمات المرور
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
# الملفات الثابتة (Static & Media)
# =========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =========================
# إعدادات تسجيل الدخول / الخروج
# =========================
LOGIN_URL = 'accounts:login'

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = '/admin_dashboard/dashboard/'
LOGOUT_REDIRECT_URL = '/'


# =========================
# إعدادات Django REST Framework
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
# إعدادات CORS (للسماح بالاتصالات)
# =========================
CORS_ALLOW_ALL_ORIGINS = True


# =========================
# القيم الافتراضية للمفاتيح الأساسية
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================
# تخصيص صفحة الخطأ الافتراضية (اختياري)
# =========================
# يمكنك إنشاء templates/404.html و 500.html لتصميم احترافي للأخطاء.
