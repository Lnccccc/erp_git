from django.shortcuts import render
from .models import orders_list,order_stat
from uuid import uuid1
from django.db.models import Count
# Create your views here.
def add_order(request):
    results = orders_list.objects.raw('select a.*,b.stat_nam from work_flow_orders_list a left join work_flow_order_stat b on a.order_status = b.stat_cd')
    order_status = order_stat.objects.all()
    tmp_list = []
    stat_1 = orders_list.objects.filter(order_status='1').aggregate(count_1=Count('order_status')).get('count_1')
    tmp_list.append(stat_1)
    stat_2 =  orders_list.objects.filter(order_status='2').aggregate(count_1=Count('order_status')).get('count_1')
    tmp_list.append(stat_2)
    stat_3 = orders_list.objects.filter(order_status='3').aggregate(count_1=Count('order_status')).get('count_1')
    tmp_list.append(stat_3)
    stat_4 = orders_list.objects.filter(order_status='4').aggregate(count_1=Count('order_status')).get('count_1')
    tmp_list.append(stat_4)
    stat_5 = orders_list.objects.filter(order_status='5').aggregate(count_1=Count('order_status')).get('count_1')
    stat_6 = orders_list.objects.filter(order_status='6').aggregate(count_1=Count('order_status')).get('count_1')
    stat_7 = orders_list.objects.filter(order_status='7').aggregate(count_1=Count('order_status')).get('count_1')
    tmp_list.append(stat_5)
    tmp_list.append(stat_6)
    tmp_list.append(stat_7)

    if request.method == 'POST':
        post = request.POST
        _client = post['client']
        _order_time = post['order_time']
        _sub_time = post['sub_time']
        _order_num = post['order_num']
        _order_detail = post['order_detail']
        _ps = post['ps']
        _person_incharge = post['person_incharge']
    ol = orders_list(uuid=uuid1(),client=_client,order_time=_order_time,sub_time=_sub_time,
                     order_num=_order_num,order_detail=_order_detail,
                     ps=_ps,order_status=2,person_incharge=_person_incharge)
    ol.save()

    return render(request,'order_list.html',context={"results":results,"count":tmp_list})
def index(request):
    tmp_list = []
    results = orders_list.objects.raw('select a.*,b.stat_nam from work_flow_orders_list a left join work_flow_order_stat b on a.order_status = b.stat_cd')
    stat_1 = orders_list.objects.filter(order_status='1').aggregate(count_1=Count('order_status')).get('count_1')
    tmp_list.append(stat_1)
    stat_2 =  orders_list.objects.filter(order_status='2').aggregate(count_1=Count('order_status')).get('count_1')
    tmp_list.append(stat_2)
    stat_3 = orders_list.objects.filter(order_status='3').aggregate(count_1=Count('order_status')).get('count_1')
    tmp_list.append(stat_3)
    stat_4 = orders_list.objects.filter(order_status='4').aggregate(count_1=Count('order_status')).get('count_1')
    tmp_list.append(stat_4)
    stat_5 = orders_list.objects.filter(order_status='5').aggregate(count_1=Count('order_status')).get('count_1')
    stat_6 = orders_list.objects.filter(order_status='6').aggregate(count_1=Count('order_status')).get('count_1')
    stat_7 = orders_list.objects.filter(order_status='7').aggregate(count_1=Count('order_status')).get('count_1')
    tmp_list.append(stat_5)
    tmp_list.append(stat_6)
    tmp_list.append(stat_7)



    return render(request,'order_list.html',context={"results":results,"count":tmp_list})
