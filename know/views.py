from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse #通过url显示执行效果，则需要导入此模块
from rest_framework import status as httpStatus
from know.models import Know
from know.models import KnowDetail
from myEnum.status import Status
import uuid

def addKnow(request):
    # desc_remark = request.GET['desc_remark']
    know = Know.objects.create(id=uuid.uuid1(),status=Status.ENABLE.value)
    return HttpResponse('增加第{}数据成功'.format(know.id))  #通过占位符format，来显示具体修改来哪行ID

def addKnowDetail(request):
    # desc_remark = request.GET['desc_remark']
    knowDetail = KnowDetail.objects.create(id=uuid.uuid1(),know_id="5070e63e-62e6-11e8-a0c3-f44d307a2894")
    return HttpResponse('增加第{}数据成功'.format(knowDetail.id))  #通过占位符format，来显示具体修改来哪行ID

def findKnowApi(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        # 如果不是的话，返回405
        return HttpResponse({'status': 'FAILED', 'data': 'only support json data'}, status=httpStatus.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'GET':
        try:
            list = []  ## 空列表
            set = Know.objects.filter(status=Status.ENABLE.value).order_by('-create_time')[:5]
            for line in set:
                item = {"id": line.id, "icon": line.icon, "status": line.status,"title": line.title,
                        "dsc_remark":line.dsc_remark,"create_time":line.create_time}
                list.append(item)
            return JsonResponse(data={'status': 'SUCCESS', 'data': list}, status=httpStatus.HTTP_200_OK)
        except Exception as why:
            print(why.args)
    # 如果不是get 请求返回不支持的请求方法
    return JsonResponse(data={'status': 'FAILED', 'data': 'GET  HTTP/1.1'}, status=httpStatus.HTTP_200_OK)

def findKnowDetailApi(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        # 如果不是的话，返回405
        return HttpResponse({'status': 'FAILED', 'data': 'only support json data'}, status=httpStatus.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'GET':
        try:
            know_id = request.GET['know_id']
            set = KnowDetail.objects.filter(know_id=know_id).order_by('c_index')
            list = []  ## 空列表
            for line in set:
                item = {"id": line.id, "icon": line.icon, "type": line.type,"context": line.context,
                        "c_index":line.c_index}
                list.append(item)
            know = {}
            k = Know.objects.get(id=know_id)# id为 know_id 的一条，多条会报错
            if k != None:
                know = {"id": k.id, "icon": k.icon, "status": k.status,"title": k.title,
                        "dsc_remark":k.dsc_remark,"create_time":k.create_time,"details":list}
            return JsonResponse(data={'status': 'SUCCESS', 'data': know}, status=httpStatus.HTTP_200_OK)
        except Exception as why:
            print(why.args)
    # 如果不是get 请求返回不支持的请求方法
    return JsonResponse(data={'status': 'FAILED', 'data': 'GET  HTTP/1.1'}, status=httpStatus.HTTP_200_OK)