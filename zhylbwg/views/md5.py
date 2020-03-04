# -*- coding: utf-8 -*-
import hashlib  # 使用hashlib模块进行md5操作


def Md5(str):
    md5 = hashlib.md5()  # 创建md5对象
    # 此处必须声明encode
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    md5.update(str.encode(encoding='utf-8'))
    # 把输入的旧密码装换为md5格式
    result = md5.hexdigest()
    # 返回加密结果
    return result
