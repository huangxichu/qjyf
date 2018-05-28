"""qjyf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from srcoll import views as srcoll_view
from homeIcon import views as home_icon_view
from api import views as api_view
from django.views.static import serve
from qjyf import settings        #upload是站点名

urlpatterns = [
    path('srcoll/add', srcoll_view.add,name="srcollAdd"),
    path('homeIcon/add', home_icon_view.add,name="homeIconAdd"),
    re_path('media/(?P<path>.*)',serve,{'document_root': settings.MEDIA_ROOT}),
    path('api/run_job',api_view.run_job),
    path('admin/', admin.site.urls),

]
