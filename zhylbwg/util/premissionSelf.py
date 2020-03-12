# -*- coding: utf-8 -*-
'''===================================
@Project：wisdomShop
@Author：班婕妤
@Date：11/3/2020 下午1:40
@Company：深圳市智慧养老宝科技有限公司
@Motto：心有猛虎，细嗅蔷薇
@Python_Version：3.7.3
@Django_Version：2.1.5
======================================='''
# 超管角色级别访问的信息
from rest_framework.permissions import BasePermission

'''
    自定义权限类的使用步骤
    （1）使用
        自己写的权限类：1.必须继承BasePermission类；  2.必须实现：has_permission方法
    （2）返回值
        True   有权访问
        False  无权访问
    （3）局部
        permission_classes = [MyPremission,] 
    （4）全局
        REST_FRAMEWORK = {
           #权限
            "DEFAULT_PERMISSION_CLASSES":['zhylbwg.utils.premission.AdminRolePremission'],
        }


'''


class AdminRolePremission(BasePermission):
    message = "必须是超级管理员角色才能访问"

    def has_permission(self, request, view):
        if request.user.user_type != 1:
            return False
        return True


# 客服角色级别访问的信息
class DocterRolePremission(BasePermission):
    message = "必须是客服角色才能访问"  # 这里的message表示如果不通过权限的时候，错误提示信息

    def has_permission(self, request, view):
        if request.user.user_type == 2 or request.user.user_type == 1:
            # False表示没有权限，提示message的信息
            # True 便是有权限，继续执行
            return False  # 若user_type 的值恒等于2 ，则表示权限不通过，输出提示message的信息
        return True


# 客服角色级别访问的信息
class AdminAndDoctorRolePremission(BasePermission):
    message = "必须是超级管理员或者医生角色才能访问"

    def has_permission(self, request, view):
        if request.user.user_type == 3:
            return False
        return True
