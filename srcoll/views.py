# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse #通过url显示执行效果，则需要导入此模块
from rest_framework import status as httpStatus
from srcoll.models import Srcoll
from myEnum.status import Status
import uuid
import json
# Create your views here.

def add(request):
    desc_remark = request.GET['desc_remark']
    a = Srcoll.objects.create(id=uuid.uuid1(),desc_remark=desc_remark,status=Status.ENABLE.value)
    return HttpResponse('增加第{}数据成功'.format(a.id))  #通过占位符format，来显示具体修改来哪行ID


def findSrcollApi(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        # 如果不是的话，返回405
        return HttpResponse({'status': 'FAILED', 'data': 'only support json data'}, status=httpStatus.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'GET':
        try:
            list = []  ## 空列表
            set = Srcoll.objects.filter(status=Status.ENABLE.value).order_by('start_time')[:3]
            for line in set:
                item = {"id": line.id, "desc_remark": line.desc_remark, "status": line.status,
                        "start_time": line.start_time, "end_time": line.end_time}
                list.append(item)
            return JsonResponse(data={'status': 'SUCCESS', 'data': list}, status=httpStatus.HTTP_200_OK)
        except Exception as why:
            print(why.args)
    # 如果不是post 请求返回不支持的请求方法
    return JsonResponse(data={'status': 'FAILED', 'data': 'GET  HTTP/1.1'}, status=httpStatus.HTTP_200_OK)
    # return HttpResponseNotAllowed(permitted_methods=['POST'])
