from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi, Welcome to UNSW Zoo home page. If you want to visit, please see bbs.unswzoo.com") 

