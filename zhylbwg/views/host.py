#-*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
from django.db import models
from zhylbwg.models.hostmodels import *
from django.views.decorators.csrf import csrf_exempt

def addhostinformationpage(request):
    return render(request,'master/host_index.html')
@csrf_exempt
def addhostinformationresult(request):
    request.encoding = 'utf-8'
    hostData = request.POST
    # hostData1 = request.body
    # print(hostData)
    # print(hostData1)
    # 你是
    if request.method == 'POST':
        print("已经进入方法")
        # f = addhostinformationresult(request.POST)  # request.POST：将接收到的数据通过Form1验证
        # if f.is_valid():  # 验证请求的内容和Form1里面的是否验证通过。通过是True，否则False。
        #     print(f.cleaned_data)  # cleaned_data类型是字典，里面是提交成功后的信息
        # else:  # 错误信息包含是否为空，或者符合正则表达式的规则
        #     print(type(f.errors), f.errors)  # errors类型是ErrorDict，里面是ul，li标签
        #     return render(request, "account/form1.html", {"error": f.errors})
        print("=========")
        print(hostData.get('hostnamep'))
        # Hostinfromation.objects.create(host_name=hostData.get("hostnamep"),host_ip=hostData.get("hostipp"),hostgroup_id=hostData.get("hostgroupg"))
        Hostinfromation(host_name=hostData.get('hostnamep'),host_ip=hostData.get('hostipp'),hostgroup=hostgroup.objects.filter('name'==hostData.get('hostgroupg')))
        # Hostinfromation(host_name='王岗1号',host_ip='192.168.1.1',hostgroup_id='2')
        #Hostinfromation.objects.create(host_name='王岗1号',host_ip='19216811',hostgroup=hostgroup.objects.filter('name'))
        Hostinfromation().save()
    return render(request,'master/login.html')

# models对于数据库的操作  增删改查
def operationsdb(request):
    # 查询数据库中的数据
    alldata = Hostinfromation.objects.all()
    data = alldata
    # 将查询到的数据传至前段，用字典类型
    return render(request,'master/login.html',{'data':alldata})