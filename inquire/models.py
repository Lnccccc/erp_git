# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BusinessDetails(models.Model):
    buyername = models.CharField(max_length=50, blank=True, null=True)
    ownerid = models.CharField(primary_key=True, max_length=50)
    openid = models.ForeignKey('User', models.DO_NOTHING, db_column='openid')
    latest_order = models.CharField(max_length=50, blank=True, null=True)
    latest_date = models.DateField()
    orders_num = models.IntegerField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    feedback_time = models.CharField(max_length=50, blank=True, null=True)
    feedback_score = models.CharField(max_length=10, blank=True, null=True)
    average_amount = models.FloatField(blank=True, null=True)
    total_task = models.IntegerField(blank=True, null=True)
    owner_url = models.CharField(max_length=250, blank=True, null=True)
    update = models.IntegerField(blank=True, null=True)
    hawkdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_details'
        unique_together = (('ownerid', 'openid'),)


class BuyerFeedback(models.Model):
    sellername = models.CharField(max_length=50, blank=True, null=True)
    ownerid = models.ForeignKey(BusinessDetails, models.DO_NOTHING, db_column='ownerid', primary_key=True)
    transaction_num = models.CharField(max_length=50, blank=True, null=True)
    transaction_url = models.CharField(max_length=250, blank=True, null=True)
    goodsurlid = models.CharField(max_length=50, blank=True, null=True)
    feedback_score = models.FloatField(blank=True, null=True)
    feedback_time = models.DateTimeField(blank=True, null=True)
    feedback_word = models.CharField(max_length=250, blank=True, null=True)
    task_num = models.IntegerField()
    hawkdate = models.DateTimeField(blank=True, null=True)
    update = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyer_feedback'
        unique_together = (('ownerid', 'task_num'),)


class EvaluateGoods(models.Model):
    goodsid = models.CharField(primary_key=True, max_length=50)
    groupid = models.ForeignKey('EvaluateGrouping', models.DO_NOTHING, db_column='groupid')
    goodsurlid = models.CharField(max_length=50)
    goodsurl = models.TextField()
    goodsname = models.CharField(max_length=50)
    flag_evaluate_monitor = models.IntegerField()
    flag_mine = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'evaluate_goods'


class EvaluateGrouping(models.Model):
    groupid = models.CharField(primary_key=True, max_length=50)
    groupname = models.CharField(max_length=50)
    openid = models.ForeignKey('User', models.DO_NOTHING, db_column='openid')

    class Meta:
        managed = False
        db_table = 'evaluate_grouping'


class EvaluateKnowledge(models.Model):
    groupid = models.CharField(max_length=50, blank=True, null=True)
    subj = models.CharField(max_length=255, blank=True, null=True)
    pred = models.CharField(max_length=255, blank=True, null=True)
    obj = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_knowledge'


class EvaluateMonitorHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupid = models.CharField(max_length=50, blank=True, null=True)
    goodsid = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    goodsname = models.CharField(max_length=50, blank=True, null=True)
    beforerate = models.IntegerField(db_column='beforeRate', blank=True, null=True)  # Field name made lowercase.
    beforenum = models.IntegerField(db_column='beforeNum', blank=True, null=True)  # Field name made lowercase.
    rate = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_monitor_history'


class EvaluatePrivateKeywords(models.Model):
    private_sort = models.ForeignKey('EvaluatePrivateSort', models.DO_NOTHING, blank=True, null=True)
    is_add_actively = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_private_keywords'


class EvaluatePrivateSort(models.Model):
    openid = models.ForeignKey('User', models.DO_NOTHING, db_column='openid')
    sort_name = models.CharField(max_length=50)
    is_add_actively = models.IntegerField()
    public_sort_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'evaluate_private_sort'


class EvaluatePublicKeywords(models.Model):
    public_keyword = models.ForeignKey('EvaluatePublicSort', models.DO_NOTHING)
    del_nums = models.IntegerField()
    keyword = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'evaluate_public_keywords'


class EvaluatePublicSort(models.Model):
    sort_name = models.CharField(max_length=255)
    is_default_sort = models.IntegerField(blank=True, null=True)
    del_nums = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_public_sort'


class EvaluateSortRelation(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    evaluate_id = models.IntegerField(blank=True, null=True)
    private_sort_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_sort_relation'


class EvaluateUrl(models.Model):
    goodsurlid = models.CharField(primary_key=True, max_length=255)
    goodsurl = models.TextField()
    bt_spider = models.IntegerField(blank=True, null=True)
    stat_spider = models.IntegerField(blank=True, null=True)
    content_err = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_url'


class EvaluateUrlDataKeyword(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    keyword = models.ForeignKey(EvaluatePrivateKeywords, models.DO_NOTHING, blank=True, null=True)
    data = models.ForeignKey('EvaluateUrldata', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_url_data_keyword'


class EvaluateUrlErr(models.Model):
    goodsurlid = models.CharField(primary_key=True, max_length=255)
    errgoodsurl = models.TextField(blank=True, null=True)
    bt_spider = models.IntegerField(blank=True, null=True)
    stat_spider = models.IntegerField(blank=True, null=True)
    content_err = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_url_err'


class EvaluateUrlErr2(models.Model):
    goodsurlid = models.CharField(primary_key=True, max_length=255)
    errgoodsurl = models.TextField(blank=True, null=True)
    bt_spider = models.IntegerField(blank=True, null=True)
    stat_spider = models.IntegerField(blank=True, null=True)
    content_err = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_url_err2'


class EvaluateUrlJudge(models.Model):
    goodsurlid = models.CharField(primary_key=True, max_length=255)
    goodsurl = models.TextField(blank=True, null=True)
    bt_spider = models.IntegerField(blank=True, null=True)
    stat_spider = models.IntegerField(blank=True, null=True)
    content_err = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_url_judge'


class EvaluateUrldata(models.Model):
    urlid = models.CharField(max_length=50, blank=True, null=True)
    user_level = models.CharField(max_length=6)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_country = models.CharField(max_length=50, blank=True, null=True)
    user_star = models.IntegerField(blank=True, null=True)
    isgood = models.IntegerField(blank=True, null=True)
    user_digg = models.IntegerField(blank=True, null=True)
    item_attr = models.CharField(max_length=255)
    logistics = models.CharField(max_length=255)
    user_review = models.TextField(blank=True, null=True)
    user_translate_review = models.TextField(blank=True, null=True)
    user_review_time = models.DateTimeField(blank=True, null=True)
    user_additional_review = models.TextField(blank=True, null=True)
    user_translate_additional_review = models.TextField(blank=True, null=True)
    user_additional_review_time = models.DateTimeField(blank=True, null=True)
    evaluate_cutting = models.TextField(blank=True, null=True)
    user_pic_view = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_urldata'


class EvaluateUrldata10(models.Model):
    urlid = models.CharField(max_length=50, blank=True, null=True)
    user_level = models.CharField(max_length=6)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_country = models.CharField(max_length=50, blank=True, null=True)
    user_star = models.IntegerField(blank=True, null=True)
    isgood = models.IntegerField(blank=True, null=True)
    user_digg = models.IntegerField(blank=True, null=True)
    item_attr = models.CharField(max_length=255)
    logistics = models.CharField(max_length=255)
    user_review = models.TextField(blank=True, null=True)
    user_translate_review = models.TextField(blank=True, null=True)
    user_review_time = models.DateTimeField(blank=True, null=True)
    user_additional_review = models.TextField(blank=True, null=True)
    user_translate_additional_review = models.TextField(blank=True, null=True)
    user_additional_review_time = models.DateTimeField(blank=True, null=True)
    evaluate_cutting = models.TextField(blank=True, null=True)
    user_pic_view = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluate_urldata_10'


class EvaluteBaseData(models.Model):
    id = models.IntegerField(primary_key=True)
    limit_sort_add_count = models.IntegerField(blank=True, null=True)
    limit_keyword_add_count = models.IntegerField(blank=True, null=True)
    default_max_url_count = models.IntegerField(blank=True, null=True)
    limit_sort_delete_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evalute_base_data'


class Goods(models.Model):
    goodsid = models.CharField(primary_key=True, max_length=255)
    groupid = models.ForeignKey('Grouping', models.DO_NOTHING, db_column='groupid')
    goodsurlid = models.CharField(max_length=50)
    goodsurl = models.TextField()
    goodsname = models.CharField(max_length=50)
    flag_price = models.IntegerField()
    flag_mine = models.IntegerField()
    urlkey = models.ForeignKey('Urlkey', models.DO_NOTHING, db_column='urlkey', blank=True, null=True)
    shopname = models.CharField(max_length=255, blank=True, null=True)
    createdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsDetail(models.Model):
    goodsurlid = models.CharField(primary_key=True, max_length=50)
    goods_name = models.CharField(max_length=250, blank=True, null=True)
    goods_category = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    goods_picture = models.CharField(max_length=250, blank=True, null=True)
    hawkdate = models.DateTimeField(blank=True, null=True)
    update = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_detail'


class Grouping(models.Model):
    groupid = models.CharField(primary_key=True, max_length=50)
    groupname = models.CharField(max_length=50)
    openid = models.ForeignKey('User', models.DO_NOTHING, db_column='openid')
    flag_warn = models.IntegerField()
    bt_wechat = models.IntegerField()
    createdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'grouping'


class StoreAllkeyword(models.Model):
    keywordid = models.AutoField(primary_key=True)
    search_heat = models.IntegerField()
    competition_degree = models.IntegerField()
    average_price = models.FloatField()
    keyword_name = models.CharField(max_length=255)
    name_1 = models.CharField(max_length=45, blank=True, null=True)
    hawkdate = models.DateTimeField(blank=True, null=True)
    auto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'store_allkeyword'


class StoreCategoryKeyword(models.Model):
    category = models.CharField(max_length=225)
    page = models.IntegerField()
    spider = models.IntegerField()
    hawkdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_category_keyword'


class StoreGoods(models.Model):
    store_urlid = models.CharField(primary_key=True, max_length=255)
    goodsurlid = models.CharField(max_length=255)
    store_url = models.CharField(max_length=255)
    goodsurl = models.CharField(max_length=255)
    hawkdate = models.DateTimeField()
    store_name = models.CharField(max_length=255)
    goods_picture = models.TextField(blank=True, null=True)
    goods_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    key_word = models.CharField(max_length=45, blank=True, null=True)
    yinliu_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_goods'
        unique_together = (('store_urlid', 'goodsurlid'),)


class StoreGoodsKeyword(models.Model):
    keywordid = models.IntegerField()
    goodsurlid = models.CharField(max_length=255)
    page = models.IntegerField()
    position = models.IntegerField()
    direct = models.IntegerField()
    hawkdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'store_goods_keyword'


class StoreNewGoods(models.Model):
    store_urlid = models.CharField(primary_key=True, max_length=255)
    store_url = models.CharField(max_length=255)
    goodsurlid = models.CharField(max_length=255)
    goodsurl = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    goods_picture = models.TextField(blank=True, null=True)
    hawkdate = models.DateTimeField()
    goods_name = models.CharField(max_length=255)
    goods_price = models.CharField(max_length=255)
    goods_order = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'store_new_goods'
        unique_together = (('store_urlid', 'goodsurlid', 'hawkdate'),)


class StoreNewGoodsDay(models.Model):
    store_urlid = models.CharField(primary_key=True, max_length=10)
    goodsurlid = models.CharField(max_length=20)
    hawkdate = models.DateField()
    keywordcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_new_goods_day'
        unique_together = (('store_urlid', 'goodsurlid'),)


class StoreUser(models.Model):
    openid = models.CharField(primary_key=True, max_length=255)
    store_urlid = models.CharField(max_length=50)
    store_url = models.CharField(max_length=255)
    comment = models.CharField(max_length=50, blank=True, null=True)
    show_number = models.IntegerField()
    comfir_spider = models.TextField(blank=True, null=True)  # This field type is a guess.
    create_date = models.DateTimeField()
    admin_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_user'
        unique_together = (('openid', 'store_urlid'),)


class Temp(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp'


class Url(models.Model):
    goodsurlid = models.CharField(primary_key=True, max_length=255)
    goodsurl = models.TextField()
    bt_spider = models.IntegerField(blank=True, null=True)
    stat_spider = models.IntegerField(blank=True, null=True)
    content_err = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url'


class UrlErr(models.Model):
    goodsurlid = models.CharField(primary_key=True, max_length=255)
    errgoodsurl = models.TextField(blank=True, null=True)
    bt_spider = models.IntegerField(blank=True, null=True)
    stat_spider = models.IntegerField(blank=True, null=True)
    content_err = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url_err'


class Urldata(models.Model):
    goodsurlid = models.CharField(max_length=50)
    price = models.FloatField()
    sale = models.IntegerField()
    praise = models.FloatField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    collect = models.IntegerField()
    c_price = models.FloatField(blank=True, null=True)
    c_praise = models.FloatField(blank=True, null=True)
    c_score = models.FloatField(blank=True, null=True)
    c_collect = models.FloatField(blank=True, null=True)
    onestar = models.IntegerField(blank=True, null=True)
    twostar = models.IntegerField(blank=True, null=True)
    threestar = models.IntegerField(blank=True, null=True)
    fourstar = models.IntegerField(blank=True, null=True)
    fivestar = models.IntegerField(blank=True, null=True)
    hawkdate = models.DateTimeField()
    t_sale = models.IntegerField(blank=True, null=True)
    t_collect = models.IntegerField(blank=True, null=True)
    t_stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'urldata'


class Urlkey(models.Model):
    urlkeyid = models.CharField(max_length=255, blank=True, null=True)
    urlnumber = models.CharField(max_length=10)
    comfir_spider = models.IntegerField()
    keyword = models.CharField(max_length=255)
    groupingid = models.ForeignKey(Grouping, models.DO_NOTHING, db_column='groupingid')
    flag_mine = models.IntegerField()
    flag_price = models.IntegerField()
    is_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'urlkey'


class User(models.Model):
    openid = models.CharField(primary_key=True, max_length=50)
    nickname = models.CharField(max_length=50)
    headimgurl = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    enterprise = models.CharField(max_length=50, blank=True, null=True)
    subscribe = models.IntegerField(blank=True, null=True)
    subscribetime = models.DateTimeField()
    sex = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    max_url = models.IntegerField()
    password = models.CharField(max_length=100, blank=True, null=True)
    evaluate_max_url = models.IntegerField()
    evaluate_current_url = models.IntegerField()
    evaluate_temp_url = models.IntegerField()
    usedurl = models.IntegerField(blank=True, null=True)
    max_store = models.IntegerField(blank=True, null=True)
    url_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
