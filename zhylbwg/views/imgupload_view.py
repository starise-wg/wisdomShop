# -*- coding: utf-8 -*-
'''===================================
@Project：wisdomShop
@Author：班婕妤
@Date：13/3/2020 下午2:27
@Company：深圳市智慧养老宝科技有限公司
@Motto：心有猛虎，细嗅蔷薇
@Python_Version：3.7.3
@Django_Version：2.1.5
======================================='''
import base64
import datetime
import json
import os

from django.http import HttpResponse

from zhylbwg.models.product import productInfo_models
from zhylbwg.views import requestResult


def image_upload(request):
    if request.method == 'POST':
        img = json.loads(request.body, encoding='utf-8')
        b64_data = img.get('product_pic')
        '''
            1:"data:image/jpg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwc
                JCQgKDBQNDAsLDBkSEw8UHRofH"
            2:base64编码图片格式为上述样式，需要截取base64,号以后的内容
        '''
        baseImg = b64_data.split(';base64,')[1]
        '''
            base64解码异常解决办法
            在解码base64字符串的时候抛异常 TypeError: Incorrect padding
        '''
        missing_padding = 4 - len(baseImg) % 4
        if missing_padding:
            baseImg += '=' * missing_padding
        # base64格式解码 需要 import base64
        base64Data = base64.b64decode(baseImg)
        # 获得当前工作目录
        root = os.path.abspath(os.curdir)
        # 设置图片保存路径
        urlPath = '\\zhylbwg\\templates\\img\\'
        # 按时间自动生成文件名称
        imgName = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + '.jpg'
        # 图片保存全路径
        imgUrl = root + urlPath + imgName
        # 打开文件
        fp = open(imgUrl, 'wb')
        # 将解码后的base64写入文件中
        fp.write(base64Data)
        '''
           将图片路径写入数据库中并保存 
        '''
        img['product_pic'] = imgUrl
        # 外键处理
        product_brand_id = img.get('product_brand_id')
        brandName = productInfo_models.BrandName.objects.filter(brand_name=product_brand_id)[0].id
        img['product_brand_id'] = productInfo_models.BrandName.objects.get(id=brandName)
        # 保存前端传入的数据
        productInfo_models.ProductInfo.objects.create(**img)
        # 返回响应
        return HttpResponse(json.dumps(requestResult.result_json('204', '图片上传成功', '')),
                            content_type="application/json,charset=utf-8")
    else:
        return HttpResponse(json.dumps(requestResult.result_json('204', '图片上传失败', '')),
                            content_type="application/json,charset=utf-8")
