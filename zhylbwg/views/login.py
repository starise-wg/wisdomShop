# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
import pandas as pd

# Create your views here.

def login(request):
    print("ok")
    return HttpResponse("深圳市智慧养老宝科技有限公司")
def pads(request):
    D = pd.DataFrame([range(1,8)],[range(2,9)])
    D.corr(method='spearman')
    S1 = D.head(0)
    S2 = D.head(1)
    s3 = S1.corr(S2,method='pearson')
    print(S1,S2,s3)
    return HttpResponse("ok")