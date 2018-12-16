# -*- coding: utf-8 -*-
from django.conf.urls import url
from login import views as login_views

urlpatterns = [
    # sso主系统相关路由
    url(r'^login$', login_views.login),
    url(r'^index$', login_views.index),
    # 主系统用户登录
    url(r'^user_login$', login_views.user_login),
    # 主系统注销登录
    url(r'^user_logout$', login_views.user_logout),




    # sso后台系统相关路由
    url(r'^back_login$', login_views.back_login),
    url(r'^back_index$', login_views.back_index),
    # 后台用户登录
    url(r'^back_user_login$', login_views.back_user_login),
    # 后台注销登录
    url(r'^back_user_logout$', login_views.back_user_logout),
    # 用户注册
    url(r'^user_register$', login_views.user_register),
    # 服务注册
    url(r'^server_register$', login_views.server_register),
    # 获取所有的服务
    url(r'^get_all_server$', login_views.get_all_server),
    # 获取所有的用户
    url(r'^get_all_user$', login_views.get_all_user),
    # 获取当前登录用户的信息
    url(r'^get_current_login_info$', login_views.get_current_login_info),
    # 校验登录的session是否过期
    url(r'^check_session_expire$', login_views.check_session_expire),
    # 用于单点的webservice
    url(r'^sso_wsdl', login_views.sso_wsdl),
]
