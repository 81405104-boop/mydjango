# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django 管理後台
    path("admin/", admin.site.urls),

    # 首頁與商品系統
    path("", include(("products.urls", "products"), namespace="products")),

    # 購物車
    path("cart/", include(("cart.urls", "cart"), namespace="cart")),

    # 帳號系統
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
]

# -------------------------------
# ✅ 開發模式下提供 static / media 檔案服務
# -------------------------------
if settings.DEBUG:
    # 從專案的 static 資料夾讀取（STATICFILES_DIRS）
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    # 讀取使用者上傳的 media 檔案
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
