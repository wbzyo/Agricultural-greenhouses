from django.shortcuts import render
from django.views.generic import View
from apps.status.models import Status
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

 #http://127.0.0.1:8000/status/device
class DeviceView(LoginRequiredMixin,View):
    '''设备状态'''
    def get(self,request):
        datas = Status.objects.all()
        params = {
            'datas':datas
        }
        return render(request,'device_status.html',params)