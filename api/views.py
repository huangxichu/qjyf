from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status as httpStatus
from myCommon.messageJson import MessageJson
from srcoll import views as srcoll_view

# Create your views here.
@csrf_exempt
def run_job(request):
    method = request.GET['method']
    if(method == 'test'):
        return test((request))
    if (method == 'findSrcoll'):
        return srcoll_view.findSrcollApi(request)
    return urlNotFound(request,method)

def test(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        # 如果不是的话，返回405
        return HttpResponse('only support json data', status=httpStatus.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'POST':
        try:
            # 解析请求的json格式入参
            data = JSONParser().parse(request)
        except Exception as why:
            print(why.args)
        else:
            content = {'msg': 'SUCCESS'}
            print(data)
            # 返回自定义请求内容content,200状态码
            return JsonResponse(data=content, status=httpStatus.HTTP_200_OK)
    # 如果不是post 请求返回不支持的请求方法
    return HttpResponseNotAllowed(permitted_methods=['POST'])

def urlNotFound(request,method):
    return JsonResponse(data={'status':'FAILED','data':'请求地址['+method+']未找到'},safe=False,status=httpStatus.HTTP_200_OK)