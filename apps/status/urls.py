from apps.status.views import DeviceView

from django.urls import path,re_path

urlpatterns = [
    path('device',DeviceView.as_view(),name='device'),

]
