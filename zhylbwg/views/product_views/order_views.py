# -*- coding: utf-8 -*-
'''===================================
@Project：wisdomShop
@Author：班婕妤
@Date：10/3/2020 下午6:09
@Company：深圳市智慧养老宝科技有限公司
@Motto：心有猛虎，细嗅蔷薇
@Python_Version：3.7.3
@Django_Version：2.1.5
======================================='''
from django.http import JsonResponse
from rest_framework.views import APIView

from zhylbwg.util.MySchemaGenerator import DocParam
from zhylbwg.util.authenticationSelf import AuthenticationSelf

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


class OrderView(APIView):
    '''订单相关业务'''
    authentication_classes = []
    permission_classes = []
    # 用coreapi_fields定义请求参数
    coreapi_fields = (
        DocParam(name="username", location='body', description='用户姓名'),
        DocParam(name="password", location='body', description='用户密码'),
        DocParam(name="telphone", location='body', description='用户手机号码', required=False),

    )
    # authentication_classes = [AuthenticationSelf,]    #添加局部认证
    def get(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None, 'data': None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)
