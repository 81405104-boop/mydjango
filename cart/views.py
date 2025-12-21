# cart/views.py
from django.shortcuts import render, redirect
from products.models import Product
from django.contrib import messages


def cart_view(request):
    """顯示購物車內容"""
    cart = request.session.get("cart", {})
    items, total = [], 0

    for pid, qty in cart.items():
        try:
            product = Product.objects.get(id=pid)
            subtotal = product.price * qty
            items.append({
                "id": product.id,
                "name": product.name,
                "image": product.image,
                "price": product.price,
                "qty": qty,
                "subtotal": subtotal
            })
            total += subtotal
        except Product.DoesNotExist:
            continue  # 若商品已刪除，略過

    return render(request, "cart/cart.html", {"items": items, "total": total})


def add_to_cart(request, pid):
    """加入購物車"""
    if request.method == "POST":
        cart = request.session.get("cart", {})
        qty = int(request.POST.get("qty", 1))
        cart[str(pid)] = cart.get(str(pid), 0) + qty
        request.session["cart"] = cart
        messages.success(request, "✅ 已加入購物車！")
    return redirect("products:home")  # ✅ 回首頁


def remove_from_cart(request, pid):
    """移除購物車中單一商品"""
    cart = request.session.get("cart", {})
    if str(pid) in cart:
        del cart[str(pid)]
        request.session["cart"] = cart
        messages.info(request, "🗑 已移除商品")
    return redirect("cart:cart_view")


def clear_cart(request):
    """清空購物車"""
    request.session["cart"] = {}
    messages.info(request, "🧹 購物車已清空")
    return redirect("cart:cart_view")


def checkout(request):
    """模擬結帳流程"""
    cart = request.session.get("cart", {})
    if not cart:
        messages.warning(request, "⚠️ 購物車是空的，無法結帳！")
        return redirect("cart:cart_view")

    total = 0
    for pid, qty in cart.items():
        try:
            product = Product.objects.get(id=pid)
            total += product.price * qty
        except Product.DoesNotExist:
            continue

    # ✅ 結帳完成後清空購物車
    request.session["cart"] = {}
    messages.success(request, f"💳 結帳完成！本次總金額 NT$ {total}")

    # ✅ 改為渲染 checkout_success.html
    return render(request, "cart/checkout_success.html", {"total": total})
