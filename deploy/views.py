from django.shortcuts import render
from juser.user_api import *
# Create your views here.


def deploy_all(request):
    # return HttpResponse("okkkk")
    if request.method == 'POST':
        print request.POST.getlist('qiantu')
        print "qqqqqq"
    return my_render('deploy/deploy_all.html', locals(), request)

def deploy_increment(request):
    # return HttpResponse("okkkk")
    if request.method == 'POST':
        print request.POST.getlist('qiantu')
        print "qqqqqq"
    return my_render('deploy/increment.html', locals(), request)

