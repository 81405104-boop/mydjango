"""
mysite/settings.py
Django 專案設定檔（開發用）
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
ALLOWED_HOSTS = []  # 上線時請設定 ['你的網域', '伺服器IP']

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
# 中介層設定
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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
        'DIRS': [BASE_DIR / 'templates'],   # 專案層級模板資料夾
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
# 靜態檔案設定（CSS / JS / 圖片）
# -----------------------------
STATIC_URL = '/static/'

# 開發環境：直接從專案資料夾載入 static
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# 上線部署時收集靜態檔案的目標資料夾
STATIC_ROOT = BASE_DIR / "staticfiles"

# -----------------------------
# 媒體檔案設定（使用者上傳）
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
