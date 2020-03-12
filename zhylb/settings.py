"""
Django settings for zhylb project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tm#!q$2$g+o)n@0xu#-5n)wzqz)sac9onnym58^3p3z&#0y+po'

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
    "zhylbwg", # 当新增App时都需要再此处进行添加
    "zhylbbjy",
    'rest_framework',
    'rest_framework_swagger',  # 用于django集成swagger
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zhylb.urls'

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

WSGI_APPLICATION = 'zhylb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
'''
    Django默认选择sqlite3数据库
'''
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
'''
    Django中配置mysql数据库
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '40.73.71.105',
        'PORT': '3306',
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '../zhylbwg/templages/img/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'img').replace('\\', '/')  # img即为图片上传的根路径
'''
    restFrameword 认证配置
'''
# 配置全局认证 REST_FRAMEWORK
REST_FRAMEWORK = {
    # 全局认证类不要放在views下
    "DEFAULT_AUTHENTICATION_CLASSES": ['zhylbwg.util.authenticationSelf.AuthenticationSelf', ],
    # 全局权限配置
    # "DEFAULT_PERMISSION_CLASSES": ['zhylbwg.util.premissionSelf.AdminAndDoctorRolePremission', ],
    # 配置全局节流
    "DEFAULT_THROTTLE_CLASSES": ['zhylbwg.util.throttle.VisitThrottle'],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
}


# swagger 配置項
# SWAGGER_SETTINGS = {
#     # 基礎樣式
#     'SECURITY_DEFINITIONS': {
#         "basic": {
#             'type': 'basic'
#         }
#     },
#     # 如果需要登錄才能夠查看接口文檔, 登錄的鏈接使用restframework自帶的.
#     'LOGIN_URL': 'rest_framework:login',
#     'LOGOUT_URL': 'rest_framework:logout',
#     # 'DOC_EXPANSION': None,
#     # 'SHOW_REQUEST_HEADERS':True,
#     # 'USE_SESSION_AUTH': True,
#     # 'DOC_EXPANSION': 'list',
#     # 接口文檔中方法列表以首字母升序排列
#     'APIS_SORTER': 'alpha',
#     # 如果支持json提交, 則接口文檔中包含json輸入框
#     'JSON_EDITOR': True,
#     # 方法列表字母排序
#     'OPERATIONS_SORTER': 'alpha',
#     'VALIDATOR_URL': None,
# }
