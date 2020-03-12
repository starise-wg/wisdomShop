# -*- coding: utf-8 -*-
from django.db import models

'''===================================
@Project：wisdomShop
@Author：班婕妤
@Date：10/3/2020 下午2:14
@Company：深圳市智慧养老宝科技有限公司
@Motto：心有猛虎，细嗅蔷薇
@Python_Version：3.7.3
@Django_Version：2.1.5
======================================='''
class Userinfo(models.Model):
    USER_TYPE = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP')
    )
    user_type = models.IntegerField(choices=USER_TYPE, blank=True, null=True)
    userName = models.CharField(max_length=10)
    userPwd = models.CharField(max_length=100)
    userTelphone = models.CharField(max_length=10)
    userAddress = models.CharField(max_length=10)
    userAge = models.CharField(max_length=4)

class UserToken(models.Model):
    user = models.OneToOneField(Userinfo, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
