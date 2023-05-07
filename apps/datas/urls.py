from apps.datas.views import NatureView,HistoryView,To_Excel
from django.urls import path,re_path

urlpatterns = [
    path('nature',NatureView.as_view(),name='nature'),
    path('history',HistoryView.as_view(),name='history'),
    path('to_excel',To_Excel.as_view(),name='to_excel'),


]
