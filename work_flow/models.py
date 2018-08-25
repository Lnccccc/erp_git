from django.db import models
# Create your models here.

class orders_list(models.Model):
    uuid = models.CharField(max_length=200,null=True)
    client = models.CharField(max_length=200,null=True)
    order_time = models.CharField(max_length=200)
    sub_time = models.CharField(max_length=200)
    order_num = models.CharField(max_length=200,null=True)
    order_detail = models.CharField(max_length=200,null=True)
    ps = models.CharField(max_length=200)
    order_status = models.IntegerField()
    person_incharge = models.CharField(max_length=100)

class order_stat(models.Model):
    stat_cd = models.IntegerField(primary_key=True)
    stat_nam = models.CharField(max_length=100)




