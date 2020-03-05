# -*- coding: utf-8 -*-
'''===================================
@Project：wisdomShop
@Author：班婕妤
@Date：5/3/2020 下午1:50
@Company：深圳市智慧养老宝科技有限公司
@Motto：心有猛虎，细嗅蔷薇
@Python_Version：3.7.3
@Django_Version：2.1.5
======================================='''
# 定义统一的json返回格式
def result_json(code, msg, data):
    # 创建一个空字典
    result = {"code": code, "msg": msg, "data": data}
    return result
