# -*- coding: utf-8 -*-
from django.db import models


class Userinfo(models.Model):
    userName = models.CharField(max_length=10)
    userPwd = models.CharField(max_length=100)
    userTelphone = models.CharField(max_length=10)
    userAddress = models.CharField(max_length=10)
    userAge = models.CharField(max_length=4)
