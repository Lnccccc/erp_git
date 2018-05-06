from django.shortcuts import render,get_object_or_404
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Keyword
from django.http  import HttpResponse
import re
from django.utils import timezone
from datetime import date
# Create your views here.

@xframe_options_exempt
def Index(request):
    return render(request,'index.html')

@xframe_options_exempt
def Getdata(request):
    def get_urlid(url):
        a = re.search(r'(.+).html?', url, re.M | re.I)
        b = a.group()[::-1]  # 将网址反转
        d = b.index('.')  # 获取第一个.的位置
        e = b.index('/'or'_')  # 获取第一个/的位置
        urlId = b[d + 1:e][::-1]  # b1就是唯一标识的ID
        return str(urlId)
    noResult = 'NO RESULT'

    date_results = []
    for i in Keyword.objects.all():
        date_results.append(i.time2)
    date_results = list(set(date_results))
    #results = get_object_or_404(Keyword.objects.filter(urlid='32808058805'))
    urlid = get_urlid(str(request.POST['id']))
    results = Keyword.objects.filter(urlid=urlid)

    if results:
        return render(request, 'detail.html', context={'results': results,"date_results":date_results})
    else:
        return render(request, 'detail.html', context={'no_result': noResult})



