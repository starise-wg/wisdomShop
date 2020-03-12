# -*- coding: utf-8 -*-
'''===================================
@Project：wisdomShop
@Author：班婕妤
@Date：11/3/2020 下午1:50
@Company：深圳市智慧养老宝科技有限公司
@Motto：心有猛虎，细嗅蔷薇
@Python_Version：3.7.3
@Django_Version：2.1.5
======================================='''
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from zhylbwg.models import loginModels
from rest_framework.request import Request
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from zhylbwg.util import premissionSelf
from zhylbwg.util.authenticationSelf import AuthenticationSelf
from zhylbwg.util.premissionSelf import DocterRolePremission
from zhylbwg.views import md5

ORDER_DICT = {
    1: {
        'name': 'apple',
        'price': 15
    },
    2: {
        'name': 'dog',
        'price': 100
    }
}


class DoctorOrderView(APIView):
    '''
    订单相关业务(只有SVIP用户才能看)
    '''
    authentication_classes = [AuthenticationSelf, ]  # 局部认证

    # permission_classes = [DocterRolePremission, ]  # 局部权限

    def get(self, request, *args, **kwargs):
        self.dispatch
        # request.user
        # request.auth
        ret = {'code': 1000, 'msg': None, 'data': None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)


class AdminAndDoctorOrderView(APIView):
    '''
    订单相关业务(只有SVIP用户才能看)
    '''

    def get(self, request, *args, **kwargs):
        self.dispatch
        # request.user
        # request.auth
        ret = {'code': 1000, 'msg': None, 'data': None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)


class CustomerRoleOrderView(APIView):
    # 配置了全局权限，此处会生效

    def get(self, request, *args, **kwargs):
        self.dispatch
        ret = {'code': 1000, 'msg': None, 'data': None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)
