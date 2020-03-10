# -*- coding: utf-8 -*-
from django.db import models


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
