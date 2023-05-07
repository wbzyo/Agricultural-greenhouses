from apps.control.views import StateControlView,PlanView

from django.urls import path,re_path

urlpatterns = [
    path('statecontrol',StateControlView.as_view(),name='statecontrol'),
    path('plan',PlanView.as_view(),name='plan'),


]
