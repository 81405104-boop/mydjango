# cart/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from products.models import Product


def _build_cart_items_and_total(cart: dict):
    """把 session cart 組成 items + total（共用）"""
    items, total = [], 0

    for pid, qty in cart.items():
        try:
            product = Product.objects.get(id=pid)
            qty = int(qty)
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
            continue

    return items, total


def cart_view(request):
    """顯示購物車內容"""
    cart = request.session.get("cart", {})
    items, total = _build_cart_items_and_total(cart)
    return render(request, "cart/cart.html", {"items": items, "total": total})


def add_to_cart(request, pid):
    """加入購物車"""
    if request.method == "POST":
        cart = request.session.get("cart", {})
        qty = int(request.POST.get("qty", 1))
        cart[str(pid)] = int(cart.get(str(pid), 0)) + qty
        request.session["cart"] = cart
        messages.success(request, "✅ 已加入購物車！")
    return redirect("products:home")


def remove_from_cart(request, pid):
    """移除購物車中單一商品"""
    if request.method == "POST":
        cart = request.session.get("cart", {})
        if str(pid) in cart:
            del cart[str(pid)]
            request.session["cart"] = cart
            messages.info(request, "🗑 已移除商品")
    return redirect("cart:cart_view")


def clear_cart(request):
    """清空購物車"""
    if request.method == "POST":
        request.session["cart"] = {}
        messages.info(request, "🧹 購物車已清空")
    return redirect("cart:cart_view")


def update_qty(request, pid):
    """AJAX 更新數量：+ / -（即時更新，不重整）"""
    if request.method != "POST":
        return JsonResponse({"ok": False, "error": "POST only"}, status=405)

    cart = request.session.get("cart", {})
    pid_str = str(pid)

    if pid_str not in cart:
        return JsonResponse({"ok": False, "error": "not in cart"}, status=404)

    action = request.POST.get("action")  # "inc" or "dec"
    qty = int(cart.get(pid_str, 1))

    if action == "inc":
        qty += 1
    elif action == "dec":
        qty = max(1, qty - 1)
    else:
        return JsonResponse({"ok": False, "error": "bad action"}, status=400)

    cart[pid_str] = qty
    request.session["cart"] = cart

    # 重新計算 subtotal / total 回傳給前端
    items, total = _build_cart_items_and_total(cart)
    subtotal = 0
    for it in items:
        if str(it["id"]) == pid_str:
            subtotal = it["subtotal"]
            break

    return JsonResponse({
        "ok": True,
        "pid": int(pid),
        "qty": qty,
        "subtotal": subtotal,
        "total": total,
    })


def checkout(request):
    """
    結帳流程：
    GET  -> 訂單摘要/付款確認頁 checkout_confirm.html
    POST -> 付款確認 -> 清空購物車 -> checkout_success.html
    """
    cart = request.session.get("cart", {})
    if not cart:
        messages.warning(request, "⚠️ 購物車是空的，無法結帳！")
        return redirect("cart:cart_view")

    items, total = _build_cart_items_and_total(cart)

    if request.method == "POST":
        # ✅ 付款確認後清空
        request.session["cart"] = {}
        pay_method = request.POST.get("pay_method", "card")
        messages.success(request, f"💳 結帳完成！付款方式：{pay_method} / 總金額 NT$ {total}")
        return render(request, "cart/checkout_success.html", {
            "total": total,
            "pay_method": pay_method
        })

    # GET：先顯示訂單摘要/付款頁
    return render(request, "cart/checkout_confirm.html", {
        "items": items,
        "total": total
    })
