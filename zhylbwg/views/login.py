# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
import pandas as pd
import json
from zhylbwg.models import loginModels
from zhylbwg.views import md5  # 导入自定义md5加密函数
from zhylbwg.views import requestResult  # 导入自定义的统一返回函数


# Create your views here.

def login(request):
    if request.method == 'POST':
        # 获取请求头数据，请求以json的格式传输
        loginInfor = request.body
        loginInformation = json.loads(loginInfor)
        # 获取用户名
        userName = loginInformation.get('userName')
        # 判断该用户名是否存在
        userNameDB = loginModels.Userinfo.objects.filter(userName=userName)
        print(userNameDB.values_list('userName')[0])
        if len(userNameDB) == 0:
            return HttpResponse(json.dumps(requestResult.result_json('202', '该用户名不存在，请注册', '')),
                                content_type="application/json,charset=utf-8")
        else:
            # 判断密码是否正确
            userPwd = loginInformation.get('userPwd')
            userPwdMd5 = md5.Md5(userPwd)
            checkLogin = loginModels.Userinfo.objects.get(userName=userName)
            if userPwdMd5 == checkLogin.userPwd:
                return HttpResponse(json.dumps(requestResult.result_json('203', '登录成功', '')),
                                    content_type="application/json,charset=utf-8")
            else:
                return HttpResponse(json.dumps(requestResult.result_json('504', '密码错误', '')),
                                    content_type="application/json,charset=utf-8")


def register(request):
    # 判断是否为post请求
    if request.method == "POST":
        # 获取请求头数据，请求以json的格式传输
        registerinformation = request.body
        # 将请求头数据转化为json格式
        registerinformationData = json.loads(registerinformation)
        # 获取用户名
        userName = registerinformationData.get('userName')
        # 从数据库中查找是否存在该用户名
        userNameDB = loginModels.Userinfo.objects.filter(userName=userName)
        # 判断用户名是否存在，若存在，则提示已有该用户，若不存在，则进行密码加密后存储到数据库中
        if len(userNameDB) != 0:
            return HttpResponse(json.dumps(requestResult.result_json('312', '该用户名已经存在', '')),
                                content_type="application/json,charset=utf-8")
        else:
            # 获取用户密码
            userPwd = registerinformationData.get('userPwd')
            # 密码加密操作md5，md5加密功能具体看md5加密代码
            userPwdMd5 = md5.Md5(userPwd)
            # 将加密后的密码赋值给请求头中的密码参数
            registerinformationData["userPwd"] = userPwdMd5
            # 将json格式数据，类型为dict 存储到数据库中，表明为Userinfo，将注册请求存储到数据库中
            loginModels.Userinfo.objects.create(**registerinformationData)
            return HttpResponse(json.dumps(requestResult.result_json('201', '注册成功，请登录', '')),
                                content_type="application/json,charset=utf-8")
    else:
        return HttpResponse(json.dumps(requestResult.result_json('501', '不是post请求', '')),
                            content_type="application/json,charset=utf-8")
