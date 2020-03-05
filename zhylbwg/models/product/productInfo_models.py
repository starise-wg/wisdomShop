# -*- coding: utf-8 -*-
from django.db import models


class BrandName(models.Model):
    brand_name = models.CharField(max_length=50, unique=True, verbose_name="品牌名称")
    brand_pic = models.ImageField(max_length=50, verbose_name='品牌logo')
    brand_company = models.CharField(max_length=50, verbose_name='品牌所属公司')


class ProductInfo(models.Model):
    product_name = models.CharField(max_length=50, unique=True, verbose_name="产品名称")  #
    product_code = models.CharField(max_length=50, verbose_name='产品编码')
    # product_brand_id = models.ForeignKey(to = "BrandName",to_field="brand_name",verbose_name='产品品牌')
    product_brand_id = models.ForeignKey(BrandName, to_field='brand_name', on_delete=models.CASCADE,
                                         verbose_name='产品品牌')
    product_pic = models.ImageField(max_length=50, verbose_name='产品图片')
    product_introduction = models.CharField(max_length=50, verbose_name='产品简介')
    product_details = models.CharField(max_length=50, verbose_name='产品详情')
    product_price = models.DecimalField(max_length=50, max_digits=6, decimal_places=1, verbose_name='产品价格')
