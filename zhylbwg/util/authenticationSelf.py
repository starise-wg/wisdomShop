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
from django.db import models
from django.http import JsonResponse
from rest_framework import exceptions
from zhylbwg.models import loginModels
from rest_framework.authentication import BaseAuthentication

#################################################
#       自定义认证类路径不能放在                 #
#       views下，可单独建立目录存放              #
#################################################
'''
    自己写认证类方法梳理
    （1）创建认证类
        继承BaseAuthentication    --->>
        1.重写authenticate方法；
        2.authenticate_header方法直接写pass就可以（这个方法必须写）
    （2）authenticate()返回值（三种）
         None ----->>>当前认证不管，等下一个认证来执行
          raise exceptions.AuthenticationFailed('用户认证失败')       # from rest_framework import exceptions
        有返回值元祖形式：（元素1，元素2）      #元素1复制给request.user;  元素2复制给request.auth
    （3）局部使用
         authentication_classes = [BaseAuthentication,]
    （4）全局使用
        #设置全局认证
        REST_FRAMEWORK = {
            "DEFAULT_AUTHENTICATION_CLASSES":['API.utils.auth.Authentication',]
        }
'''


class AuthenticationSelf(BaseAuthentication):
    '''认证'''

    def authenticate(self, request):
        print("========")
        print(request)
        token = request._request.GET.get('token')
        # print(token)
        token_obj = loginModels.UserToken.objects.filter(token=token).first()
        # print(token_obj)
        # print(token_obj.user.userName)
        # print(token_obj)
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败-请申请认证')
        # 在rest framework内部会将这两个字段赋值给request，以供后续操作使用
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        pass
