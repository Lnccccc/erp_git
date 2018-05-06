from django.urls import path
from . import views
app_name = 'inquire'
urlpatterns = [
    path('index/',views.Index,name='index'),
    path('detail/',views.Getdata,name='Getdata')
]