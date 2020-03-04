# -*- coding: utf-8 -*-
# 定义统一的json返回格式
def result_json(code, msg, data):
    # 创建一个空字典
    result = {"code": code, "msg": msg, "data": data}
    return result
