from pathlib import Path
import os  # 用於靜態檔與模板的路徑拼接

# ================================
# 📌 專案基本設定
# ================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ 正式環境請將 SECRET_KEY 移到環境變數
SECRET_KEY = 'django-insecure-your-secret-key'

# 開發階段建議為 True，上線請改 False
DEBUG = True

# 允許訪問的主機列表
ALLOWED_HOSTS = ['mydjango-jpmm.onrender.com']


# ================================
# 📌 App 設定
# ================================
INSTALLED_APPS = [
    # Django 內建 App
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 自訂 App
    'pages',   # ← 你的主網站頁面
]


# ================================
# 📌 Middleware 設定
# ================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ================================
# 📌 URL & WSGI 設定
# ================================
ROOT_URLCONF = 'myprofile_site.urls'
WSGI_APPLICATION = 'myprofile_site.wsgi.application'


# ================================
# 📌 Template 設定
# ================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 讓 Django 能在專案根目錄下的 templates 資料夾找 HTML
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


# ================================
# 📌 資料庫設定（預設 SQLite）
# ================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ================================
# 📌 密碼驗證設定（預設即可）
# ================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ================================
# 📌 語系與時區設定
# ================================
LANGUAGE_CODE = 'en-us'        # 語系
TIME_ZONE = 'Asia/Taipei'      # 時區
USE_I18N = True
USE_TZ = True


# ================================
# 📌 靜態檔案設定
# ================================
STATIC_URL = 'static/'

# 設定靜態檔案收集的目錄
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 用來收集靜態檔案的資料夾
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# ================================
# 📌 媒體檔案設定（可用於上傳圖片）
# ================================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ================================
# 📌 其他設定
# ================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
