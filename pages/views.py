from django.shortcuts import render

# 📌 首頁 View
def home(request):
    """
    首頁 View
    對應 templates/pages/home.html
    """
    # 成員資料（暫時寫死，未來可改用資料庫）
    members = [
        {"name": "張小軒", "id": "p1", "img": "images/p1.jpg"},
        {"name": "王小明", "id": "p2", "img": "images/p2.jpg"},
        {"name": "張大同", "id": "p3", "img": "images/p3.jpg"},
        {"name": "林依依", "id": "p4", "img": "images/p4.jpg"},
        {"name": "陳阿華", "id": "p5", "img": "images/p5.jpg"},
        {"name": "黃志強", "id": "p6", "img": "images/p6.jpg"},
    ]
    return render(request, 'pages/home.html', {"members": members})


# 📌 關於我 View
def about(request):
    """
    關於我 View
    對應 templates/pages/about.html
    """
    return render(request, 'pages/about.html')


# 📌 聯絡我 View
def contact(request):
    """
    聯絡我 View
    對應 templates/pages/contact.html
    """
    return render(request, 'pages/contact.html')


# 📌 成員個人介紹頁面
def member_detail(request, member_id):
    """
    成員詳細介紹頁
    例如：http://127.0.0.1:8000/member/p1/
    """
    member_profiles = {
        "p1": {
            "name": "張小軒",
            "img": "images/p1.jpg",
            # ✨ 中英文合併，使用 <br> 換行
            "intro": "大家好，我是張小軒，我喜歡撿電線、收集電線，還有打籃球！<br>Hi everyone, I'm Zhang Xiaoxuan. I like collecting wires and playing basketball!🏀"
        },
        "p2": {
            "name": "王小明",
            "img": "images/p2.jpg",
            "intro": "嗨～我是王小明，興趣是 跟著張董撿電線，也熱愛旅遊。",
        },
        "p3": {
            "name": "張大同",
            "img": "images/p3.jpg",
            "intro": "我是張大同，對 AI 技術和資料分析非常感興趣！",
        },
        "p4": {
            "name": "林依依",
            "img": "images/p4.jpg",
            "intro": "大家好，我喜歡前端設計，也熱愛攝影與旅遊。",
        },
        "p5": {
            "name": "陳阿華",
            "img": "images/p5.jpg",
            "intro": "哈囉～我是陳阿華，我擅長後端開發，也愛打遊戲。",
        },
        "p6": {
            "name": "黃志強",
            "img": "images/p6.jpg",
            "intro": "嗨～我是黃志強，我喜歡學習新技術，也常參加黑客松。",
        },
    }

    profile = member_profiles.get(member_id)
    if not profile:
        # 若找不到該成員，導向一個「找不到頁面」
        return render(request, 'pages/member_not_found.html', {"member_id": member_id})

    return render(request, 'pages/member_detail.html', {"profile": profile})
