from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from mealapp import models
register = template.Library()

@register.filter(name='members')
def MemberInfo(request):
    member  = models.MemberInfo.objects.filter(status = True).all()
    return member

@register.filter(name='months')
def Month(request):
    month  = models.Month.objects.filter(status = True).all()
    return month

@register.filter(name='contactreg')
def mycontact(request):
    cnt  = models.Contact.objects.filter(Status = True).order_by("-id")
    return cnt




@register.filter(name='str2url')
def string_to_url_convert(data):
    #use in view: category = cat.replace('-', ' ')
    # use in html: text|str2url
    data = str(data)    
    return data.replace(' ', '-') 

@register.filter(name='replace')
def replace_load(obj):
    rep = obj.replace("%20"," ")
    return rep
