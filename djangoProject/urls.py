"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from cmdb import views  # 导入对应app的视图文件
from . import view

urlpatterns = [
    path('hello/', view.hello),
    url(r'^admin/', admin.site.urls),  # 后台管理页面
    url(r"^main/", views.main),  # app路由 url(regex, view, kwargs=None, name=None)
    url(r"^$", views.welcome),
    url(r"^login/", views.login),
]
