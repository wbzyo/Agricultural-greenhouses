from django.shortcuts import render,redirect,reverse
from django.http.response import JsonResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.control.models import ControlEexel
import time

# Create your views here.

# http://127.0.0.1:8000/control/statecontrol
class StateControlView(LoginRequiredMixin,View):
    '''状态控制'''
    def get(self,request):
        control_excel = ControlEexel.objects.filter(is_delete=0)
        contexts ={
            'control_excel':control_excel
        }
        return render(request,'state_control.html',contexts)

    def post(self,request):
        place = request.POST.get('place')
        print(place+"************")
        depth = request.POST.get('depth')
        date = request.POST.get('date')
        starttime = request.POST.get('starttime')
        stoptime = request.POST.get('stoptime')
        if stoptime > starttime:
            try:
                ControlEexel.objects.create(auto_flag=1, place=place, tu_depth=depth, grow_circle=date,
                                            start_time=starttime, stop_time=stoptime)
            except ControlEexel.DoesNotExist:
                return redirect(reverse('control:statecontrol'))# 计划错误
            return redirect(reverse('control:statecontrol'))# 计划正确
        else:
            redirect(reverse('control:statecontrol'))# 计划错误


class PlanView(View):
    '''计划删除'''
    def post(self,request):
        id = request.POST.get('id')
        try:
            control_excel = ControlEexel.objects.get(id=id)
        except ControlEexel.DoesNotExist:
            return JsonResponse({'res': 1,'errmsg':'失败'})
        control_excel.is_delete = 1
        control_excel.save()
        return JsonResponse({'res':3})