from django.shortcuts import render
from django.http import JsonResponse, HttpResponse #通过url显示执行效果，则需要导入此模块
from rest_framework import status as httpStatus
from product.models import ProductBase
from myEnum.status import Status
import uuid

def addProductBase(request):
    base = ProductBase.objects.create(id=uuid.uuid1(),status=Status.ENABLE.value)
    return HttpResponse('增加第{}数据成功'.format(base.id))  #通过占位符format，来显示具体修改来哪行ID

def findProductBase(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        # 如果不是的话，返回405
        return HttpResponse({'status': 'FAILED', 'data': 'only support json data'}, status=httpStatus.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'GET':
        try:
            offset = int(request.GET['offset'])
            skip = int(request.GET['skip'])
            list = []  ## 空列表
            set = ProductBase.objects.filter(status=Status.ENABLE.value).order_by('-create_time')[offset:skip]
            for line in set:
                item = {"id": line.id, "icon": line.icon, "status": line.status,"name": line.name,
                        "desc_remark":line.desc_remark,"create_time":line.create_time}
                list.append(item)
            return JsonResponse(data={'status': 'SUCCESS', 'data': list}, status=httpStatus.HTTP_200_OK)
        except Exception as why:
            print(why.args)
    # 如果不是get 请求返回不支持的请求方法
    return JsonResponse(data={'status': 'FAILED', 'data': 'GET  HTTP/1.1'}, status=httpStatus.HTTP_200_OK)