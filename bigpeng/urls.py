"""bigpeng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from bigpeng import settings

urlpatterns = [
    #http://127.0.0.1:8000/news/luntan
    #http://127.0.0.1:8000/admin/   后台
    path('admin/', admin.site.urls),
    path('user/',include(('apps.user.urls','apps.user'),namespace='user')),
    #path('user/',include('apps.user.urls'),
    path('status/', include(('apps.status.urls','apps.status'),namespace='status')),
    path('news/', include(('apps.news.urls','news'),namespace='news')),
    path('datas/', include(('apps.datas.urls','apps.datas'),namespace='datas')),
    path('control/', include(('apps.control.urls','apps.control'),namespace='control')),
    path('tinymce/',include('tinymce.urls')),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# 拼接图片的地址
# urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)