from django.contrib import admin
from apps.news.models import News,NewsInfo,Comment,NewsSwiper
from apps.user.models import User
from apps.control.models import ControlEexel,FuzzySearch,XiData
from apps.status.models import Status
from apps.datas.models import AirData,GroundData

# 自定义显示标题
class MyAdminSite(admin.AdminSite):
    site_header = '农业大棚智能管理系统'  # 此处设置页面显示标题
    site_title = '大棚'  # 此处设置页面头部标题

admin_site = MyAdminSite(name='management')
# Register your models here.
admin.site.register(News)
admin.site.register(NewsInfo)
admin.site.register(User)
admin.site.register(ControlEexel)
admin.site.register(FuzzySearch)
admin.site.register(XiData)
admin.site.register(Status)
admin.site.register(AirData)
admin.site.register(GroundData)
admin.site.register(Comment)
admin.site.register(NewsSwiper)
admin.site.site_header = '农业大棚智能管理系统'
admin.site.site_title = '大棚'







