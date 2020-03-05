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
import json
from zhylbwg.models.product import productInfo_models
from django.shortcuts import HttpResponse
from zhylbwg.views import requestResult
from django.core import serializers  # 导入序列化的包


def add_product(request):
    requestInformation = request.body
    productInformation = json.loads(requestInformation, encoding='utf-8')
    product_brand_id = productInformation.get('product_brand_id')
    brandName = productInfo_models.BrandName.objects.filter(brand_name=product_brand_id)[0].id
    productInformation['product_brand_id'] = productInfo_models.BrandName.objects.get(id=brandName)
    print(productInformation)
    if request.method == 'POST':
        productInfo_models.ProductInfo.objects.create(**productInformation)
        return HttpResponse(json.dumps(requestResult.result_json('204', '产品新增成功', '')),
                            content_type="application/json,charset=utf-8")


def query_product(request):
    requestInformation = request.body
    productInformation = json.loads(requestInformation, encoding='utf-8')
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
                                             productInfo_models.ProductInfo.objects.filter(product_name=porductName))
        return HttpResponse(json.dumps(requestResult.result_json('205', '查询成功', quere_result)),
                            content_type="application/json,charset=utf-8")


def add_brand(request):
    requestInformation = request.body
    brandInformation = json.loads(requestInformation, encoding='utf-8')
    if request.method == 'POST':
        productInfo_models.BrandName.objects.create(**brandInformation)
        return HttpResponse(json.dumps(requestResult.result_json('204', '品牌新增成功', '')),
                            content_type="application/json,charset=utf-8")
