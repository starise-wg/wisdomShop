"""zhylb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from zhylbwg.views import login # 导入相关APP下的views文件
from zhylbwg.views import host # 导入相关APP下的views文件
from django.views.generic.base import RedirectView

from zhylbwg.views.product_views import product_information_views
from zhylbwg.views.auth_views import AuthView
from zhylbwg.views.premission_views import *

# 导入coreapi相关模块
from rest_framework.documentation import include_docs_urls
# 导入自定义的schema
from zhylbwg.util.MySchemaGenerator import SwaggerSchemaView
# 自定义接口
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from zhylbwg.views.product_views.order_views import OrderView

schema_view = get_schema_view(title='班婕妤API接口文档', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
router = routers.DefaultRouter()

urlpatterns = [
    # favicon.cio
    path('favicon.ico/', RedirectView.as_view(url=r'static/blog/img/favicon.ico')),
    path('admin/', admin.site.urls),
    path('zhylbwg/login', login.login),
    # swagger接口文档路由
    path("zhylbwg/docs", SwaggerSchemaView.as_view()),
    # path("zhylbwg/docs", schema_view,name = 'docs'), # 配置docs的url路径
    path('', include(router.urls)),  # 代表位于根路径的主域名(http://127.0.0.1:8080
    # drf登录
    path('zhylbwg/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 测试接口
    path('zhylbwg/test1', AuthView.as_view(), name='test1'),

    # path('login/',  ),

    # zhylbwg
    path('host/',host.addhostinformationpage),
    path('host/add/',host.addhostinformationresult),
    path('host/check/', host.operationsdb),
    path('zhylbwg/register/', login.register),
    path('zhylbwg/login/', login.login),
    path('zhylbwg/addproduct/', product_information_views.PorductOpertion.add_product),  # 新增商品
    path('zhylbwg/addbrand/', product_information_views.PorductOpertion.add_brand),  # 新增商品
    path('zhylbwg/queryProduct/', product_information_views.PorductOpertion.query_product),  # 查询商品
    path('zhylbwg/image/', product_information_views.PorductOpertion.image_upload),  # 上传图片

    #  '''
    #         Django的url是将一个请求分配给可调用的函数的，而不是一个class。针对这个问题，
    #         class-based view提供了一个as_view()静态方法（也就是类方法），调用这个方法，
    #         会创建一个类的实例，然后通过实例调用dispatch()方法，dispatch()方法会根据request
    #         的method的不同调用相应的方法来处理request（如get() , post()等）。到这里，这
    #         些方法和function-based view差不多了，要接收request，得到一个response返回。如果
    #         方法没有定义，会抛出HttpResponseNotAllowed异常。
    #
    #     '''
    path('zhylbwg/auth/', AuthView.as_view()),  # 生成token
    path('zhylbwg/authe/', OrderView.as_view()),  # 订单视图
    # 角色权限控制
    path('zhylbwg/per/admin/', AuthView.as_view(), ),  # 生成token
    path('zhylbwg/per/doctor/', DoctorOrderView.as_view()),  # 医生权限测
    path('zhylbwg/per/customer/', CustomerRoleOrderView.as_view()),  # 医生权限测
    # path('zhylbwg/per/adminAndDoctor/', AdminAndDoctorOrderView.as_view()),  # 超管和医生权限


    path('meizi/', host.zhihuMeiZI),
    # BeautifulSoup练习
    path('bsi/', host.Bsi)


]
