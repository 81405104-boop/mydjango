# cart/urls.py
from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_view, name="cart_view"),
    path("add/<int:pid>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:pid>/", views.remove_from_cart, name="remove_from_cart"),
    path("clear/", views.clear_cart, name="clear_cart"),

    # ✅ 即時更新數量
    path("update/<int:pid>/", views.update_qty, name="update_qty"),

    # ✅ 結帳：先摘要/付款頁，再成功頁
    path("checkout/", views.checkout, name="checkout"),
]
