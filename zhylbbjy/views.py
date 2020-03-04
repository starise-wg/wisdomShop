from django.shortcuts import render,HttpResponse

# Create your views here.

def login(request):
    name = """zhang,
    lishi
    """

    print('ok')
    return HttpResponse('深圳市智慧养老宝科技有限公司23')


