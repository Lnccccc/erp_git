from django.urls import path
from . import  views
app_name = 'work_flow'
urlpatterns = [
    path("",views.index,name="index"),
    path("add_order/",views.add_order,name='add_order'),
    path("status_<int:status_cd>/",views.status,name='status')
]