from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status as httpStatus
from myCommon.messageJson import MessageJson
from srcoll import views as srcoll_view
from homeIcon import views as home_icon_view
from know import views as know_view
from product import productBaseView as product_base_view
import time
from myCommon.myMd5 import md5
# Create your views here.

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


key = 'dsadsadasdasdasdsdsdsdsd'
visited_keys = {

}
def api_auth(func):
    def inner(request,*args,**kwargs):
        server_float_ctime = time.time()
        auth_header_val = request.META.get('HTTP_AUTH_API')
        client_md5_str,client_ctime = auth_header_val.split('|',maxsplit = 1)
        client_float_ctime = float(client_ctime)

        #1
        if (client_float_ctime + 20) < server_float_ctime:
            return JsonResponse(data={'status': 'FAILED', 'data': '请求过期'}, safe=False,
                                status=httpStatus.HTTP_200_OK)

        #2
        server_md5_str = md5("%s|%s" % (key,client_ctime,))
        if(server_md5_str != client_md5_str):
            return JsonResponse(data={'status': 'FAILED', 'data': '无效的key'}, safe=False,
                                status=httpStatus.HTTP_200_OK)
        #3
        if visited_keys.get(client_md5_str):
            return JsonResponse(data={'status': 'FAILED', 'data': '已经访问了'}, safe=False,
                                status=httpStatus.HTTP_200_OK)

        visited_keys[client_md5_str] = client_float_ctime
        return func(request,*args,**kwargs)
    return inner

@csrf_exempt
# @api_auth
def run_job(request):
    method = request.GET['method']
    if(method == 'test'):
        return test((request))
    if (method == 'findSrcoll'):
        return srcoll_view.findSrcollApi(request)
    if (method == 'findHomeIcon'):
        return home_icon_view.findHomeIconApi(request)
    if (method == 'findKnow'):
        return know_view.findKnowApi(request)
    if (method == 'findKnowDetail'):
        return know_view.findKnowDetailApi(request)
    if (method == 'findProductBase'):
        return product_base_view.findProductBase(request)
    return urlNotFound(request,method)
