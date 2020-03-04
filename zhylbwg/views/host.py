#-*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
from django.db import models
from zhylbwg.models.hostmodels import *
from django.views.decorators.csrf import csrf_exempt
import requests  # 爬虫框架
from bs4 import BeautifulSoup  # 利用BeautifulSoup对原始网页进行解析
import re
import urllib.request

def addhostinformationpage(request):
    return render(request,'master/host_index.html')
@csrf_exempt
def addhostinformationresult(request):
    request.encoding = 'utf-8'
    hostData = request.POST
    # hostData1 = request.body
    # print(hostData)
    # print(hostData1)
    # 你是
    if request.method == 'POST':
        print("已经进入方法")
        # f = addhostinformationresult(request.POST)  # request.POST：将接收到的数据通过Form1验证
        # if f.is_valid():  # 验证请求的内容和Form1里面的是否验证通过。通过是True，否则False。
        #     print(f.cleaned_data)  # cleaned_data类型是字典，里面是提交成功后的信息
        # else:  # 错误信息包含是否为空，或者符合正则表达式的规则
        #     print(type(f.errors), f.errors)  # errors类型是ErrorDict，里面是ul，li标签
        #     return render(request, "account/form1.html", {"error": f.errors})
        print("=========")
        print(hostData.get('hostnamep'))
        # Hostinfromation.objects.create(host_name=hostData.get("hostnamep"),host_ip=hostData.get("hostipp"),hostgroup_id=hostData.get("hostgroupg"))
        Hostinfromation(host_name=hostData.get('hostnamep'),host_ip=hostData.get('hostipp'),hostgroup=hostgroup.objects.filter('name'==hostData.get('hostgroupg')))
        # Hostinfromation(host_name='王岗1号',host_ip='192.168.1.1',hostgroup_id='2')
        #Hostinfromation.objects.create(host_name='王岗1号',host_ip='19216811',hostgroup=hostgroup.objects.filter('name'))
        Hostinfromation().save()
    return render(request,'master/login.html')

# models对于数据库的操作  增删改查
def operationsdb(request):
    # 查询数据库中的数据
    alldata = Hostinfromation.objects.all()
    data = alldata
    # 将查询到的数据传至前端，用字典类型
    return render(request,'master/login.html',{'data':alldata})


# 批量爬取知乎妹子图片
def zhihuMeiZI(request):
    url = 'http://www.mzitu.com/zipai/'
    # 此处User-Agent属性不能带省略号  不然会报错 UnicodeEncodeError: 'latin-1' codec can't encode character '\u2026' in position 30: ordinal not in range(256)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; ) Gecko/20100101 Firefox/64.0'}
    r = requests.get(url, headers=header)
    text = r.text
    # 利用Beautifulsoul对网页进行解析
    bsl = BeautifulSoup(r.content, 'html5lib')
    meiziResult = bsl.prettify()
    # 找出所有的img标签
    for link in bsl.find_all('img'):
        tupian = "data-actualsrc"
        print(link.tupian)

    return render(request, 'master/meizi.html', {"meizitupian": meiziResult})


def meiziTuPian(request):
    # 打开网页，获取网页内容
    def url_open(url):
        headers = ("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
        return data

    # 获取自拍栏目总的页面数
    def get_num(url):
        data = url_open(url)
        # 页面源代码中通过正则表达匹配出总的页码数
        pat = "<span class='page-numbers current'>(.+?)</span>"
        num = re.compile(pat).findall(data)[0]
        return num

    if __name__ == '__main__':
        try:  # 爬取的起始页面地址
            url = 'http://www.mzitu.com/zipai/'
            num = get_num(url)
            for i in range(1, int(num) + 1):
                # 自拍栏目每一页页面的地址
                page_url = 'http://www.mzitu.com/zipai/comment-page-' + str(i)
                # 自拍栏目每一页中，通过正则表达匹配出图片地址
                img_pat = '<p><img src="(.+?)"'
                data = url_open(page_url)
                img_list = re.compile(img_pat).findall(data)
                # 依次遍历出每一页获取到的图片地址，并将图片下载到本地
                for j in range(len(img_list)):
                    img_url = img_list[j]
                    img = "img/meizi_" + str(i) + str(j) + ".jpg"
                    print("正在下载第" + str(i) + "页，第" + str(j) + "个图片")
                    urllib.request.urlretrieve(img_url, img)
                    print("第" + str(i) + str(j) + "个图片下载完成")
                    # urlcleanup()清理使用urlretrieve产生的缓存
                urllib.request.urlcleanup()
        except Exception as e:
            print(e)
    return render(request, 'master/login.html', {'data': 'ok'})


'''
    BeautifalSoul使用
'''


def Bsi(request):
    url = "http://www.mzitu.com/zipai/"
    # 将本地 index.html 文件打开，用它来创建 soup 对象
    # bsi = BeautifulSoup(open("master/BeautifulSoulIndex.html"))
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; ) Gecko/20100101 Firefox/64.0'}
    zipai = requests.get(url, headers=header)
    bsizipai = BeautifulSoup(zipai.content, "html.parser")
    font = bsizipai.find_all('img', 'src').string
    print(font)
    data = bsizipai
    return render(request, 'master/BeautifulSoulIndex.html', {'data': data})
