from django.shortcuts import render,get_object_or_404
from django.views.decorators.clickjacking import xframe_options_exempt
from datetime import date
import time
from .models import keyword3
from django.http  import HttpResponse
import re
from django.utils import timezone
import datetime
# Create your views here.

@xframe_options_exempt
def Index(request):
    return render(request,'detail.html')

@xframe_options_exempt
def Getdata(request):
    def get_urlid(url):
        a = re.search(r'(.+).html?', url, re.M | re.I)
        b = a.group()[::-1]  # 将网址反转
        d = b.index('.')  # 获取第一个.的位置
        e = b.index('/'or'_')  # 获取第一个/的位置
        urlId = b[d + 1:e][::-1]  # b1就是唯一标识的ID
        return str(urlId)
    noResult = '您所查询的行业数据尚未开放，想查看更多商品关键词数据，欢迎关注微信公众号：微分析，联系客服QQ:3325993794，官方q群：538014809'
    latest_results = []
    date_results = []
    keyword_results = []
    #for i in keyword3.objects.all():
        #if i.updatatime.strftime("%y-%m-%d") not in date_results:
            #date_results.append(i.updatatime.strftime("%y-%m-%d"))

    #results = get_object_or_404(Keyword.objects.filter(urlid='32808058805'))
    post_id = str(request.POST['id'])
    try:
        urlid = get_urlid(post_id)
    except:
        wrong_url = '您输入的商品链接有误，请输入正确的速卖通商品链接'
        return render(request,'detail.html',context={'wrong_url':wrong_url})
    results = keyword3.objects.filter(urlid=urlid).order_by('-keyword')
    for i in results:
        if i.updatatime.strftime("%y-%m-%d") not in date_results:
            date_results.append(i.updatatime.strftime("%y-%m-%d"))
    for i in results:
        if i.updatatime.strftime("%y-%m-%d") == date_results[0]:
            latest_results.append(i)
    for i in latest_results:
        if i.keyword not in keyword_results:
            keyword_results.append(i)

    #for i in results:
        #if i.updatatime.strftime("%y-%m-%d") == date_results[-1]:
            #latest_results.append(i)
    if results:
        return render(request, 'detail.html', context={'results': latest_results,"date_results":date_results})
    else:
        return render(request, 'detail.html', context={'no_result': noResult})



