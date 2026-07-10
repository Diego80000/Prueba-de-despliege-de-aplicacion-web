from pathlib import Path
<<<<<<< HEAD
import os
=======
>>>>>>> 090201e781a4e766aaa226bc99f6e51436e1d25c

# Directorio Base
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD
SECRET_KEY = 'django-insecure-1idk2)1km2=+)$ys56yu$azc0g9=g*!(pe*k^2#i57g^o)+4b)'
DEBUG = True
<<<<<<< HEAD
ALLOWED_HOSTS = []
=======
ALLOWED_HOSTS = ['*']
>>>>>>> 090201e781a4e766aaa226bc99f6e51436e1d25c

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'seguridad_unellez',  
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

ROOT_URLCONF = 'mi_proyecto.urls'

<<<<<<< HEAD
# CONFIGURACIÓN DE PLANTILLAS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # Django buscará en las carpetas 'templates' de cada app automáticamente
        'APP_DIRS': True, # Esto es lo que permite usar 'seguridad_unellez/templates/'
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
=======
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'seguridad_unellez' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
>>>>>>> 090201e781a4e766aaa226bc99f6e51436e1d25c
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mi_proyecto.wsgi.application'

# Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Caracas'
USE_I18N = True
USE_TZ = True

<<<<<<< HEAD
# Archivos estáticos y multimedia
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de Login
=======
# Archivos estáticos
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =============================================================================
# CONFIGURACIONES DE AUTENTICACIÓN Y MENSAJES
# =============================================================================

>>>>>>> 090201e781a4e766aaa226bc99f6e51436e1d25c
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'lista_guardias'
LOGOUT_REDIRECT_URL = 'login'

<<<<<<< HEAD
# Estilos de mensajes
=======
# Estilos para que los mensajes de Django coincidan con CSS/Bootstrap
>>>>>>> 090201e781a4e766aaa226bc99f6e51436e1d25c
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

<<<<<<< HEAD
# Configuración de Correo
=======
# =============================================================================
# CONFIGURACIÓN DE CORREO (GMAIL SMTP)
# =============================================================================

>>>>>>> 090201e781a4e766aaa226bc99f6e51436e1d25c
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'carloslionel15angel@gmail.com'
<<<<<<< HEAD
EMAIL_HOST_PASSWORD = 'odoe mrek aeym fhtz' 
DEFAULT_FROM_EMAIL = f'Seguridad UNELLEZ <{EMAIL_HOST_USER}>'

PASSWORD_RESET_TIMEOUT = 14400 
=======
EMAIL_HOST_PASSWORD = 'odoe mrek aeym fhtz'  
DEFAULT_FROM_EMAIL = f'Seguridad UNELLEZ <{EMAIL_HOST_USER}>'

# Seguridad de Tokens (4 horas de duración)
PASSWORD_RESET_TIMEOUT = 14400 

# Evita conflictos con pre-escaneo de enlaces en el navegador
>>>>>>> 090201e781a4e766aaa226bc99f6e51436e1d25c
SECURE_CROSS_ORIGIN_OPENER_POLICY = None