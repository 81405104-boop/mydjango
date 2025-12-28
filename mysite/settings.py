"""
mysite/settings.py
Django 購物網站設定檔（開發／cpolar 部署用 + Whitenoise 加速）
"""

from pathlib import Path

# -----------------------------
# 專案根目錄設定
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# 安全設定
# -----------------------------
SECRET_KEY = 'dev-secret-key-change-me'   # ⚠️ 上線時請改用環境變數儲存
DEBUG = True

# ✅ 允許的 Host（本機 + cpolar 網域）
ALLOWED_HOSTS = [
    '192.168.1.145',
    'localhost',
    '127.0.0.1',
    'moontv.hk.cpolar.io',
    'django1.tw.cpolar.io',
    'django2.tw.cpolar.io',
]

# ✅ CSRF 信任來源
CSRF_TRUSTED_ORIGINS = [
    'http://192.168.1.145',
    'http://localhost',
    'http://127.0.0.1',
    'https://moontv.hk.cpolar.io',
    'https://django1.tw.cpolar.io',
    'https://django2.tw.cpolar.io',
]

# -----------------------------
# 已安裝的 App
# -----------------------------
INSTALLED_APPS = [
    # Django 內建
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 自訂 App
    'products',
    'cart',
    'accounts',
]

# -----------------------------
# 中介層設定（Whitenoise 加速）
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ 加速 static file
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# URL 進入點
# -----------------------------
ROOT_URLCONF = 'mysite.urls'

# -----------------------------
# 模板設定
# -----------------------------
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

# -----------------------------
# WSGI / ASGI
# -----------------------------
WSGI_APPLICATION = 'mysite.wsgi.application'
ASGI_APPLICATION = 'mysite.asgi.application'

# -----------------------------
# 資料庫設定（預設 SQLite）
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------
# 密碼驗證
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    # ⚠️ 正式上線請解除註解
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------
# 語系與時區
# -----------------------------
LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_TZ = True

# -----------------------------
# 靜態檔案設定
# -----------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ Whitenoise 加速設定
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MAX_AGE = 31536000  # 📦 圖片 / CSS / JS 快取一年（秒）

# -----------------------------
# 媒體檔案設定
# -----------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -----------------------------
# 預設主鍵型別
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------
# 登入 / 登出導向
# -----------------------------
LOGIN_REDIRECT_URL = "/"   # 登入後回首頁
LOGOUT_REDIRECT_URL = "/"  # 登出後回首頁

# -----------------------------
# 📧（可選）Email 設定
# -----------------------------
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your_email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your_app_password'

# -----------------------------
# 附加說明（開發提示）
# -----------------------------
"""
💡 靜態檔案資料夾建議結構：

E:\mydjango\
│
├─ static\
│   ├─ css\
│   │   └─ style.css
│   ├─ images\
│   │   ├─ flags\
│   │   │   ├─ nepal_flag.png
│   │   │   └─ taiwan_flag.png
│   │   └─ bg\
│   │       └─ mandala_pattern.png
│   └─ js\
│
└─ media\     ← 使用者上傳檔案（自動建立）
"""
