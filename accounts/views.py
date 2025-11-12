from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_view(request):
    """صفحة تسجيل الدخول"""
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            return HttpResponse(f'<h1>مرحباً {user.username}! تم تسجيل الدخول بنجاح</h1><a href="/django-admin/">اذهب للوحة التحكم</a>')
        else:
            error_msg = '<p style="color:red">اسم المستخدم أو كلمة المرور غير صحيحة</p>'
    else:
        error_msg = ''
    
    html = f'''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>تسجيل الدخول</title>
        <style>
            body {{ font-family: Arial; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; display: flex; align-items: center; justify-content: center; margin: 0; }}
            .container {{ background: white; padding: 40px; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); width: 400px; }}
            h1 {{ text-align: center; color: #333; margin-bottom: 30px; }}
            input {{ width: 100%; padding: 12px; margin-bottom: 15px; border: 2px solid #ddd; border-radius: 8px; font-size: 16px; box-sizing: border-box; }}
            button {{ width: 100%; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 8px; font-size: 18px; font-weight: bold; cursor: pointer; }}
            .test {{ margin-top: 20px; padding: 15px; background: #f5f5f5; border-radius: 8px; text-align: center; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔐 تسجيل الدخول</h1>
            {error_msg}
            <form method="POST">
                <input type="text" name="username" placeholder="اسم المستخدم" required>
                <input type="password" name="password" placeholder="كلمة المرور" required>
                <button type="submit">دخول</button>
            </form>
            <div class="test">
                <strong>حساب تجريبي:</strong><br>
                admin / admin123
            </div>
        </div>
    </body>
    </html>
    '''
    
    return HttpResponse(html)


def home(request):
    """الصفحة الرئيسية"""
    if request.user.is_authenticated:
        return HttpResponse('<h1>مرحباً! أنت مسجل دخول</h1>')
    return redirect('/admin_dashboard/dashboard/')



@login_required
def logout_view(request):
    """تسجيل الخروج"""
    logout(request)
    return redirect('accounts:login')