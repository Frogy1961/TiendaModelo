"""
Django settings for modelstore project.
Configuración adaptada para Render deployment y desarrollo local.
"""

from pathlib import Path
import os
import sys

# dotenv + decouple + dj-database-url
from dotenv import load_dotenv
from decouple import config
import dj_database_url

# ----------------------------
# BASE_DIR
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# LOGGING (opcional, útil para ver salida en consola)
# ----------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
        },
    },
    "root": {"handlers": ["console"], "level": "DEBUG"},
}

# ----------------------------
# Cargar variables de entorno (.env.local prioriza)
# ----------------------------
# Si existe .env.local lo carga (tu Mac), si no existe intenta .env (producción/Render)
env_local = BASE_DIR / ".env.local"
env_prod = BASE_DIR / ".env"

if env_local.exists():
    load_dotenv(dotenv_path=str(env_local))
elif env_prod.exists():
    load_dotenv(dotenv_path=str(env_prod))
# Ahora las variables de entorno están en os.environ y se leen con decouple.config()

# ----------------------------
# SECRET / DEBUG / ALLOWED_HOSTS
# ----------------------------
# SECRET_KEY debe definirse en .env o .env.local
SECRET_KEY = config("SECRET_KEY", default="unsafe-secret-key-for-dev-only")
DEBUG = config("DEBUG", cast=bool, default=False)

# Ajusta hosts permitidos; añade el dominio de Render (ej: tiendamodelo.onrender.com)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost,127.0.0.1").split(",")
# ejemplo: en .env puedes poner ALLOWED_HOSTS=tiendamodelo.onrender.com,localhost

# Para Render HTTPS (si usas dominios con subdominios)
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="").split(",") if config("CSRF_TRUSTED_ORIGINS", default="") else []

# ----------------------------
# APPS
# ----------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps del proyecto
    "website",
    "servicios",
    "blog",
    "contacto",
    "tienda",
    "carro",
    "user",
    "pedidos",
    # de terceros
    "crispy_forms",
    "crispy_bootstrap5",
]

# ----------------------------
# MIDDLEWARE
# ----------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # sirve static en producción
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "modelstore.urls"

# ----------------------------
# TEMPLATES
# ----------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Puedes mantener BASE_DIR / "templates" si tienes templates globales.
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "carro.context_processor.importe_total_carro",
            ],
        },
    },
]

WSGI_APPLICATION = "modelstore.wsgi.application"

# ----------------------------
# DATABASES
# ----------------------------
# Si no existe DATABASE_URL en .env, por defecto usa sqlite local
default_db_url = config("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")

DATABASES = {
    "default": dj_database_url.parse(default_db_url, conn_max_age=600, ssl_require=not DEBUG)
}

# ----------------------------
# PASSWORD VALIDATORS
# ----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ----------------------------
# I18N / TIMEZONE
# ----------------------------
LANGUAGE_CODE = "es-MX"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ----------------------------
# STATIC & MEDIA
# ----------------------------
STATIC_URL = '/static/'
# Carpetas donde trabajas assets en desarrollo
STATICFILES_DIR = [
    'website/static',
    ]
# Carpeta donde collectstatic dejará archivos para servir en producción
STATIC_ROOT = BASE_DIR / 'static'
# Whitenoise storage recomendado en producción
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ----------------------------
# EMAIL
# ----------------------------
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = config("EMAIL_HOST", default="smtp.gmail.com")
    EMAIL_PORT = config("EMAIL_PORT", cast=int, default=587)
    EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=True)
    EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")

# ----------------------------
# CRISPY FORMS
# ----------------------------
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ----------------------------
# MENSAJES
# ----------------------------
from django.contrib.messages import constants as mensajes_de_error

MESSAGE_TAGS = {
    mensajes_de_error.DEBUG: "debug",
    mensajes_de_error.INFO: "info",
    mensajes_de_error.SUCCESS: "success",
    mensajes_de_error.WARNING: "warning",
    mensajes_de_error.ERROR: "danger",
}

# ----------------------------
# OTROS
# ----------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
