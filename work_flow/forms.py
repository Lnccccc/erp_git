from django import forms
from django.contrib.admin import widgets
class WorkFlowForm(forms.Form):
    client = forms.CharField(max_length=200)
    order_time = forms.DateField(widget=widgets.AdminDateWidget())
    sub_time = forms.DateField(widget=widgets.AdminDateWidget())
    order_num = forms.CharField(label='order number',max_length=200)
    order_detail = forms.CharField(label='order detail',max_length=200)
    ps = forms.CharField(label='ps',max_length=200)
    person_incharge = forms.CharField(label='person_incharge',max_length=200)

