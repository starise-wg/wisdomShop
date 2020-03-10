# -*- coding: utf-8 -*-
'''===================================
@Project：wisdomShop
@Author：班婕妤
@Date：10/3/2020 下午2:14
@Company：深圳市智慧养老宝科技有限公司
@Motto：心有猛虎，细嗅蔷薇
@Python_Version：3.7.3
@Django_Version：2.1.5
======================================='''
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from zhylbwg.models.auth import auth_models
from zhylbwg.views import md5
from django.views import View
from zhylbwg.models import loginModels

'''
    用户验证，当用户首次登录时随机生成一个token
'''


class AuthView(View):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        print("=======")
        try:
            print("=======")
            user = request.POST.get('username')
            print(user)
            pwd = md5.Md5(request.POST.get('password'))
            print(pwd)
            obj = loginModels.Userinfo.objects.filter(userName=user, userPwd=pwd).first()
            print(obj)
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
            # 为用户创建token
            token = md5.Md5(user)
            print(token)
            # 存在就更新，不存在就创建
            loginModels.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)
