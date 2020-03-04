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
from django.urls import path
from zhylbwg.views import login # 导入相关APP下的views文件
from zhylbwg.views import host # 导入相关APP下的views文件
import zhylbbjy
from django.views.generic.base import RedirectView

urlpatterns = [
    # favicon.cio
    path('favicon.ico/', RedirectView.as_view(url=r'static/blog/img/favicon.ico')),
    path('admin/', admin.site.urls),
    path('zhylbwg/login', login.login),
    # path('login/',  ),

    # zhylbwg
    path('host/',host.addhostinformationpage),
    path('host/add/',host.addhostinformationresult),
    path('host/check/', host.operationsdb),
    path('zhylbwg/register/', login.register),
    path('zhylbwg/login/', login.login),
    # 爬取知乎妹子图片

    path('meizi/', host.zhihuMeiZI),
    # BeautifulSoup练习
    path('bsi/', host.Bsi)


]
