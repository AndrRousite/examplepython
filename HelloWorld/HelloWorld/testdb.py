#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/25 15:24
import random
import string

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from TestModel.models import Test
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'


def test(request):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    data = Test(name=salt)
    data.save()
    return HttpResponse("<p>数据添加成功：" + salt + "</p>")


# 查询数据
def query(request):
    context = {}
    arr = Test.objects.all()
    context['arr'] = arr
    return render(request, 'test.html', context)
    pass


# 更新
def update(request):
    context = {}
    url = 'update.html'
    if request.POST:
        arr = Test.objects.all()
        arr.update(name=''.join(random.sample(string.ascii_letters + string.digits, 8)))
        context['arr'] = arr
        url = 'test.html'
    return render(request, url, context)


def search(request):
    request.encoding = 'utf-8'
    context = {}
    if 'q' in request.GET:
        arr = Test.objects.filter(name=request.GET['q']).order_by('id')
        context['arr'] = arr
    return render(request, 'search.html', context)
