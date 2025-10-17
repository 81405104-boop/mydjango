from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # 新增成員介紹頁面
    path('member/<str:member_id>/', views.member_detail, name='member_detail'),
]
