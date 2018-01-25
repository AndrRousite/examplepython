#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/25 14:41
from django.shortcuts import render

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'


def index(request):
    print(request)
    result = {'name': '过滤器的参数跟随冒号之后并且总是以双引号包含。 例如： {{ bio|truncatewords:"30" }} 这个将显示变量 bio 的前30个词。', 'value': 1234}
    return render(request, 'index.html', result)
