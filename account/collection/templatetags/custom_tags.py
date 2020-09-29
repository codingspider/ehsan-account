from django import template
from django.db.models import Sum

register = template.Library()
from ..models import FeesCollection, FeesGroupFeeType, FeeGroups, FeesType, StudentFeesMaster


@register.simple_tag(takes_context=True)
def subtractify(context, obj):

    feestypes = StudentFeesMaster.objects.get(pk=obj)
    fee_able = feestypes.amount
    student_id = feestypes.student_id
    queryset = FeesCollection.objects.filter(student_id=student_id, fees_group=obj)
    data = queryset.aggregate(all_sum=Sum('paid_amount'))['all_sum']
    newval = fee_able - data
    return newval


@register.simple_tag(takes_context=True)
def totalpaid(context, obj):
    feestypes = StudentFeesMaster.objects.get(pk=obj)
    student_id = feestypes.student_id
    queryset = FeesCollection.objects.filter(student_id=student_id, fees_group=obj)
    data = queryset.aggregate(all_sum=Sum('paid_amount'))['all_sum']
    newval = data
    return newval


