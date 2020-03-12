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
import base64
import datetime
import json
import os

from rest_framework import generics
from rest_framework.views import APIView

from zhylbwg.models.product import productInfo_models
from django.shortcuts import HttpResponse, render
from zhylbwg.views import requestResult
from django.core import serializers  # 导入序列化的包
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from zhylbwg.views.serializers import UserSerializer, GroupSerializer


class PorductOpertion(viewsets.ModelViewSet, APIView):
    def add_product(request):
        productInformation = json.loads(request.body, encoding='utf-8')
        product_brand_id = productInformation.get('product_brand_id')
        brandName = productInfo_models.BrandName.objects.filter(brand_name=product_brand_id)[0].id
        productInformation['product_brand_id'] = productInfo_models.BrandName.objects.get(id=brandName)
        print(productInformation)
        if request.method == 'POST':
            productInfo_models.ProductInfo.objects.create(**productInformation)
            return HttpResponse(json.dumps(requestResult.result_json('204', '产品新增成功', '')),
                                content_type="application/json,charset=utf-8")

    def query_product(request):
        productInformation = json.loads(request.body, encoding='utf-8')
        if request.method == 'POST':
            porductName = productInformation.get('product_name')
            '''
                1:在Django框架中，我们不能直接将QuerySet对象通过 HttpResponse(json.dumps(QeurySet))返回给前端Ajax....
                    否则会报错：Object of type 'QuerySet' is not JSON serializable
                2:因此需要序列号后才能返回给前端Ajax....
                    serializers.serialize("json",productInfo_models.ProductInfo.objects.filter(product_name=porductName))
                    jango.core import serializers 
            '''
            quere_result = serializers.serialize("json",
                                                 productInfo_models.ProductInfo.objects.filter(
                                                     product_name=porductName))
            return HttpResponse(json.dumps(requestResult.result_json('205', '查询成功', quere_result)),
                                content_type="application/json,charset=utf-8")

    def add_brand(request):
        brandInformation = json.loads(request.body, encoding='utf-8')
        if request.method == 'POST':
            productInfo_models.BrandName.objects.create(**brandInformation)
            return HttpResponse(json.dumps(requestResult.result_json('204', '品牌新增成功', '')),
                                content_type="application/json,charset=utf-8")

    '''
        图片上传功能
        1：前端页面将图片转化为base64编码，通过json数据传输
        2：后端解码后将数据写入img文件
    '''

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
