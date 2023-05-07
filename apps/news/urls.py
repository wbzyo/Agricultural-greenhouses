
from apps.news.views import LuntanView,WriteView,DetailView
from django.urls import path,re_path

urlpatterns = [
    path('luntan',LuntanView.as_view(),name='luntan'),
    path('write',WriteView.as_view(),name='write'),
    re_path('detail/(?P<id>\d+)',DetailView.as_view(),name='detail'),

]
