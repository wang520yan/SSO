# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from spyne.server.django import DjangoApplication
from login.com.const_variables import sso_login_check
from login.com.trans_data import *
from login.com.web_service import application
from login.data_operation.server_operation import ServerOperation
from login.data_operation.sso_session_operation import SSOSessionOperation
from login.data_operation.user_operation import UserOperation
from login.models import UsersModels


def login(request):
    """
    返回登录页面
    :param request:
    :return:
    """
    if request.session.get('username2'):
        return HttpResponseRedirect("/index")
    else:
        return render(request, 'login/login.html')


def index(request):
    """
    返回系统页面
    :param request:
    :return:
    """
    return render(request, 'login/index.html')


def user_login(request):
    """
    用户登录
    :param request:
    :return:
    """
    result = {}
    receive_data = trans_user_login(request)
    username = receive_data.get('username')
    password = receive_data.get('password')
    UOP = UserOperation()
    user_info = UOP.login_check_user(username, password)
    # user = auth.authenticate(username=username, password=password)
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    session_info = {}
    session_info['session_username'] = username
    session_info['session_ip'] = ip
    if user_info.get('flag'):
        verify = True
        # auth.login(request, user)
        SSP = SSOSessionOperation()
        SSP.add_session(session_info)
    else:
        verify = False
    result['result'] = verify
    return JsonResponse(result)


def user_logout(request):
    """
    用户注销
    :param request:
    :return:
    """
    result = {}
    auth.logout(request)
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    SSP = SSOSessionOperation()
    SSP.delete_session(ip)
    username = SSP.check_login_by_ip(ip)
    if username:
        result['logout'] = False
    else:
        result['logout'] = True
    return JsonResponse(result)


def back_login(request):
    """
    返回登录页面
    :param request:
    :return:
    """
    if request.session.get('username1'):
        return HttpResponseRedirect("/index")
    else:
        return render(request, 'login/back_login.html')


@sso_login_check
def back_index(request):
    """
    返回系统页面
    :param request:
    :return:
    """
    return render(request, 'login/back_index.html')


def back_user_login(request):
    """
    后台用户登录
    :param request:
    :return:
    """
    result = {}
    receive_data = trans_user_login(request)
    username = receive_data.get('username')
    password = receive_data.get('password')
    UOP = UserOperation()
    user_info = UOP.login_check_user(username, password)
    # user = auth.authenticate(username=username, password=password)
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    session_info = {}
    session_info['session_username'] = username
    session_info['session_ip'] = ip
    if user_info.get('flag'):
        verify = True
        # auth.login(request, user)
        SSP = SSOSessionOperation()
        SSP.add_session(session_info)
    else:
        verify = False
    result['result'] = verify
    return JsonResponse(result)


def back_user_logout(request):
    """
    后台用户注销
    :param request:
    :return:
    """
    result = {}
    auth.logout(request)
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    SSP = SSOSessionOperation()
    SSP.delete_session(ip)
    username = SSP.check_login_by_ip(ip)
    if username:
        result['logout'] = False
    else:
        result['logout'] = True
    return JsonResponse(result)



def user_register(request):
    """
    用户的注册
    :param request:
    :return:
    """
    result = {}
    receive_data = trans_user_register(request)
    username = receive_data.get('username')
    if not receive_data['password'] == receive_data['password_confirmation']:
        result['flag'] = False
        result['msg'] = '密码不一致'
        return JsonResponse(result)
    UOP = UserOperation()
    try:
        UOP.add_user(receive_data)
        result['flag'] = True
        result['msg'] = username + ' 注册成功'
    except Exception as e:
        print e.message
        result['msg'] = e.message
        result['flag'] = False
    return JsonResponse(result)


def server_register(request):
    """
    服务的注册
    :param request:
    :return:
    """
    result = {}
    receive_data = trans_server_register(request)
    SOP = ServerOperation()
    data = SOP.add_server(receive_data)
    result['data'] = data
    return JsonResponse(result)


def get_all_server(request):
    """
    获取所有注册的服务
    :param request:
    :return:
    """
    result = {}
    SOP = ServerOperation()
    data = SOP.get_all_servers()
    result['data'] = data
    return JsonResponse(result)


def get_all_user(request):
    """
    获取所有的用户
    :param request:
    :return:
    """
    result = {}
    SOP = UserOperation()
    data = SOP.get_all_user()
    result['data'] = data
    return JsonResponse(result)


def get_current_login_info(request):
    """
    获取当前登录用户信息
    :param request:
    :return:
    """
    result = {}
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    SSP = SSOSessionOperation()
    username = SSP.check_login_by_ip(ip)
    if username == '':
        result['code'] = 400
        result['message'] = '已注销'
        return JsonResponse(result)
    else:
        result['code'] = 200
        result['username'] = username
        result['message'] = '用户信息'
        return JsonResponse(result)


def check_session_expire(request):
    """
    校验登录的session是否过期
    :param request:
    :return:
    """
    result = {}
    SSP = SSOSessionOperation()
    SSP.check_session_expire_time()
    return JsonResponse(result)



sso_wsdl = csrf_exempt(DjangoApplication(application))
