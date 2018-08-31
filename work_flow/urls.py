from django.urls import path
from . import  views
app_name = 'work_flow'
urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("add_order/",views.add_order,name='add_order'),
    path("status/<int:status_cd>/",views.status,name='status'),
    path("delete/<str:uuidd>/",views.delete_order,name='delete'),
    path("update/<str:uuidd>/",views.update_order,name='update')
]