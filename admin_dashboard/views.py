from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'admin_dashboard/dashboard.html')



    
    # إحصائيات
    total_users = User.objects.count()
    total_admins = User.objects.filter(role__in=['SUPER_ADMIN', 'ADMIN']).count()
    total_employees = User.objects.filter(role='EMPLOYEE').count()
    total_clients = User.objects.filter(role='CLIENT').count()
    
    html = f'''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>لوحة التحكم - نظام ERP</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
            * {{ font-family: 'Cairo', sans-serif; }}
            
            .card-hover {{
                transition: all 0.3s ease;
            }}
            .card-hover:hover {{
                transform: translateY(-5px);
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
            }}
            
            .gradient-bg {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }}
        </style>
    </head>
    <body class="bg-gray-50">
        
        <!-- Sidebar -->
        <aside class="fixed right-0 top-0 h-screen w-64 bg-white shadow-xl z-50">
            <div class="gradient-bg p-6 text-white">
                <div class="flex items-center space-x-3 space-x-reverse">
                    <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center">
                        <i class="fas fa-chart-line text-indigo-600 text-xl"></i>
                    </div>
                    <div>
                        <h1 class="text-xl font-bold">نظام ERP</h1>
                        <p class="text-sm opacity-80">إدارة متكاملة</p>
                    </div>
                </div>
            </div>
            
            <div class="p-4 border-b">
                <div class="flex items-center space-x-3 space-x-reverse">
                    <img src="https://ui-avatars.com/api/?name={request.user.username}&background=6366f1&color=fff&size=40" 
                         class="w-10 h-10 rounded-full" alt="User">
                    <div>
                        <p class="font-semibold text-gray-800">{request.user.username}</p>
                        <p class="text-xs text-gray-500">مدير النظام</p>
                    </div>
                </div>
            </div>
            
            <nav class="p-4 space-y-2">
                <a href="/admin/dashboard/" class="flex items-center space-x-3 space-x-reverse p-3 rounded-lg text-gray-700 bg-indigo-50 border-r-4 border-indigo-600">
                    <i class="fas fa-home w-5"></i>
                    <span class="font-semibold">الرئيسية</span>
                </a>
                
                <a href="/admin/users/" class="flex items-center space-x-3 space-x-reverse p-3 rounded-lg text-gray-700 hover:bg-gray-50">
                    <i class="fas fa-users w-5"></i>
                    <span>المستخدمون</span>
                </a>
                
                <a href="/admin/products/" class="flex items-center space-x-3 space-x-reverse p-3 rounded-lg text-gray-700 hover:bg-gray-50">
                    <i class="fas fa-boxes w-5"></i>
                    <span>المخزون</span>
                </a>
                
                <a href="/admin/sales/" class="flex items-center space-x-3 space-x-reverse p-3 rounded-lg text-gray-700 hover:bg-gray-50">
                    <i class="fas fa-shopping-cart w-5"></i>
                    <span>المبيعات</span>
                </a>
                
                <a href="/admin/purchases/" class="flex items-center space-x-3 space-x-reverse p-3 rounded-lg text-gray-700 hover:bg-gray-50">
                    <i class="fas fa-shopping-bag w-5"></i>
                    <span>المشتريات</span>
                </a>
                
                <a href="/admin/hr/" class="flex items-center space-x-3 space-x-reverse p-3 rounded-lg text-gray-700 hover:bg-gray-50">
                    <i class="fas fa-user-tie w-5"></i>
                    <span>الموارد البشرية</span>
                </a>
                
                <a href="/admin/accounting/" class="flex items-center space-x-3 space-x-reverse p-3 rounded-lg text-gray-700 hover:bg-gray-50">
                    <i class="fas fa-calculator w-5"></i>
                    <span>المحاسبة</span>
                </a>
                
                <a href="/admin/reports/" class="flex items-center space-x-3 space-x-reverse p-3 rounded-lg text-gray-700 hover:bg-gray-50">
                    <i class="fas fa-chart-bar w-5"></i>
                    <span>التقارير</span>
                </a>
                
                <a href="/admin/settings/" class="flex items-center space-x-3 space-x-reverse p-3 rounded-lg text-gray-700 hover:bg-gray-50">
                    <i class="fas fa-cog w-5"></i>
                    <span>الإعدادات</span>
                </a>
                
                <a href="/accounts/logout/" class="flex items-center space-x-3 space-x-reverse p-3 rounded-lg text-red-600 hover:bg-red-50">
                    <i class="fas fa-sign-out-alt w-5"></i>
                    <span>تسجيل الخروج</span>
                </a>
            </nav>
        </aside>
        
        <!-- Main Content -->
        <main class="mr-64 p-8">
            
            <!-- Header -->
            <header class="mb-8">
                <div class="flex items-center justify-between">
                    <div>
                        <h2 class="text-3xl font-bold text-gray-800">مرحباً بك، {request.user.username}! 👋</h2>
                        <p class="text-gray-600 mt-1">إليك ملخص أداء النظام اليوم</p>
                    </div>
                    
                    <div class="flex items-center space-x-4 space-x-reverse">
                        <button class="relative p-2 text-gray-600 hover:bg-gray-100 rounded-full">
                            <i class="fas fa-bell text-xl"></i>
                            <span class="absolute top-0 right-0 w-3 h-3 bg-red-500 rounded-full"></span>
                        </button>
                        
                        <div class="text-right">
                            <p class="text-sm text-gray-600">التاريخ</p>
                            <p class="font-semibold text-gray-800">الثلاثاء، 12 نوفمبر 2024</p>
                        </div>
                    </div>
                </div>
            </header>
            
            <!-- Stats Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                
                <div class="card-hover bg-white rounded-xl p-6 shadow-lg">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-gray-500 text-sm mb-1">إجمالي المستخدمين</p>
                            <h3 class="text-3xl font-bold text-gray-800">{total_users}</h3>
                            <p class="text-green-500 text-sm mt-2">
                                <i class="fas fa-arrow-up"></i>
                                <span>نشط</span>
                            </p>
                        </div>
                        <div class="w-16 h-16 bg-gradient-to-br from-blue-400 to-blue-600 rounded-full flex items-center justify-center">
                            <i class="fas fa-users text-white text-2xl"></i>
                        </div>
                    </div>
                </div>
                
                <div class="card-hover bg-white rounded-xl p-6 shadow-lg">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-gray-500 text-sm mb-1">المديرون</p>
                            <h3 class="text-3xl font-bold text-gray-800">{total_admins}</h3>
                            <p class="text-purple-500 text-sm mt-2">
                                <i class="fas fa-shield-alt"></i>
                                <span>إدارة</span>
                            </p>
                        </div>
                        <div class="w-16 h-16 bg-gradient-to-br from-purple-400 to-purple-600 rounded-full flex items-center justify-center">
                            <i class="fas fa-user-shield text-white text-2xl"></i>
                        </div>
                    </div>
                </div>
                
                <div class="card-hover bg-white rounded-xl p-6 shadow-lg">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-gray-500 text-sm mb-1">الموظفون</p>
                            <h3 class="text-3xl font-bold text-gray-800">{total_employees}</h3>
                            <p class="text-blue-500 text-sm mt-2">
                                <i class="fas fa-briefcase"></i>
                                <span>فريق العمل</span>
                            </p>
                        </div>
                        <div class="w-16 h-16 bg-gradient-to-br from-green-400 to-green-600 rounded-full flex items-center justify-center">
                            <i class="fas fa-user-tie text-white text-2xl"></i>
                        </div>
                    </div>
                </div>
                
                <div class="card-hover bg-white rounded-xl p-6 shadow-lg">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-gray-500 text-sm mb-1">العملاء</p>
                            <h3 class="text-3xl font-bold text-gray-800">{total_clients}</h3>
                            <p class="text-orange-500 text-sm mt-2">
                                <i class="fas fa-handshake"></i>
                                <span>عملاء نشطون</span>
                            </p>
                        </div>
                        <div class="w-16 h-16 bg-gradient-to-br from-orange-400 to-orange-600 rounded-full flex items-center justify-center">
                            <i class="fas fa-users text-white text-2xl"></i>
                        </div>
                    </div>
                </div>
                
            </div>
            
            <!-- Quick Actions -->
            <div class="bg-white rounded-xl p-6 shadow-lg mb-8">
                <h3 class="text-xl font-bold text-gray-800 mb-4">إجراءات سريعة</h3>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                    
                    <button class="flex flex-col items-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition">
                        <i class="fas fa-user-plus text-blue-600 text-2xl mb-2"></i>
                        <span class="text-sm font-semibold text-gray-700">إضافة مستخدم</span>
                    </button>
                    
                    <button class="flex flex-col items-center p-4 bg-green-50 rounded-lg hover:bg-green-100 transition">
                        <i class="fas fa-box text-green-600 text-2xl mb-2"></i>
                        <span class="text-sm font-semibold text-gray-700">إضافة منتج</span>
                    </button>
                    
                    <button class="flex flex-col items-center p-4 bg-purple-50 rounded-lg hover:bg-purple-100 transition">
                        <i class="fas fa-file-invoice text-purple-600 text-2xl mb-2"></i>
                        <span class="text-sm font-semibold text-gray-700">فاتورة جديدة</span>
                    </button>
                    
                    <button class="flex flex-col items-center p-4 bg-orange-50 rounded-lg hover:bg-orange-100 transition">
                        <i class="fas fa-chart-line text-orange-600 text-2xl mb-2"></i>
                        <span class="text-sm font-semibold text-gray-700">عرض التقارير</span>
                    </button>
                    
                </div>
            </div>
            
            <!-- Recent Activity -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                
                <div class="bg-white rounded-xl p-6 shadow-lg">
                    <h3 class="text-xl font-bold text-gray-800 mb-4">النشاط الأخير</h3>
                    <div class="space-y-4">
                        <div class="flex items-center space-x-3 space-x-reverse p-3 bg-gray-50 rounded-lg">
                            <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                                <i class="fas fa-user text-blue-600"></i>
                            </div>
                            <div class="flex-1">
                                <p class="font-semibold text-gray-800">مستخدم جديد انضم</p>
                                <p class="text-sm text-gray-500">منذ 5 دقائق</p>
                            </div>
                        </div>
                        
                        <div class="flex items-center space-x-3 space-x-reverse p-3 bg-gray-50 rounded-lg">
                            <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center">
                                <i class="fas fa-shopping-cart text-green-600"></i>
                            </div>
                            <div class="flex-1">
                                <p class="font-semibold text-gray-800">طلب جديد تم إضافته</p>
                                <p class="text-sm text-gray-500">منذ 15 دقيقة</p>
                            </div>
                        </div>
                        
                        <div class="flex items-center space-x-3 space-x-reverse p-3 bg-gray-50 rounded-lg">
                            <div class="w-10 h-10 bg-purple-100 rounded-full flex items-center justify-center">
                                <i class="fas fa-file-invoice text-purple-600"></i>
                            </div>
                            <div class="flex-1">
                                <p class="font-semibold text-gray-800">فاتورة تم دفعها</p>
                                <p class="text-sm text-gray-500">منذ ساعة</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white rounded-xl p-6 shadow-lg">
                    <h3 class="text-xl font-bold text-gray-800 mb-4">إشعارات النظام</h3>
                    <div class="space-y-4">
                        <div class="p-3 bg-yellow-50 border-r-4 border-yellow-400 rounded">
                            <p class="font-semibold text-gray-800">تحذير: مخزون منخفض</p>
                            <p class="text-sm text-gray-600">3 منتجات تحتاج إلى إعادة تعبئة</p>
                        </div>
                        
                        <div class="p-3 bg-green-50 border-r-4 border-green-400 rounded">
                            <p class="font-semibold text-gray-800">نجاح: نسخة احتياطية</p>
                            <p class="text-sm text-gray-600">تمت النسخة الاحتياطية بنجاح</p>
                        </div>
                        
                        <div class="p-3 bg-blue-50 border-r-4 border-blue-400 rounded">
                            <p class="font-semibold text-gray-800">معلومة: تحديث متاح</p>
                            <p class="text-sm text-gray-600">إصدار جديد من النظام متوفر</p>
                        </div>
                    </div>
                </div>
                
            </div>
            
        </main>
        
    </body>
    </html>
    '''
    
    return HttpResponse(html)