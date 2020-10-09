from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("你好哇， 这是UNSWZoo的首页, 还在开发哦。校内论坛请转 <a>bbs.unswzoo.com</a>") 

