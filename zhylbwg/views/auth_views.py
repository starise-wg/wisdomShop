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
from rest_framework.decorators import api_view
from zhylbwg.models.auth import auth_models
from zhylbwg.util.MySchemaGenerator import DocParam
from zhylbwg.views import md5
from django.views import View
from zhylbwg.models import loginModels
'''
    用户验证，当用户首次登录时随机生成一个token
'''
# CBV 视图模式
class AuthView(APIView):
    '''
        post：
        为用户生成token的方法
    '''
    authentication_classes = []
    permission_classes = []
    coreapi_fields = (
        DocParam(name="username", location='body', description='用户姓名'),
        DocParam(name="password", location='body', description='用户密码'),
    )

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            user = request.POST.get('username')
            pwd = md5.Md5(request.POST.get('password'))
            obj = loginModels.Userinfo.objects.filter(userName=user, userPwd=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
            # 为用户创建token
            token = md5.Md5(user)
            # 存在就更新，不存在就创建
            loginModels.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)
