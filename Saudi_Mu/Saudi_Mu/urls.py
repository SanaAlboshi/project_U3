from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية من تطبيق main
    path('', include('main.urls')),

    path('account/', include('account.urls')),
    path('contact/', include('contact.urls')),
    path('museum/', include('museum.urls')),
]
