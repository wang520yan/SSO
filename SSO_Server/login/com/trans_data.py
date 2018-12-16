# -*- coding: utf-8 -*-

def trans_user_login(request):
    """
        用于解析前端传送的登录账号信息内容
        :return:
        """
    result = {}
    if request.method == 'POST':
        result = {'username': request.POST.get('username'),
                  'password': request.POST.get('passwd')
                  }
    return result


def trans_server_register(request):
    """
    用于解析前端传送的注册服务的信息
    :param request:
    :return:
    """
    result = {}
    if request.method == 'POST':
        result = {'server_name': request.POST.get('server_name', ''),
                  'server_name_en': request.POST.get('server_name_en', ''),
                  'server_description': request.POST.get('server_description', ''),
                  'server_url': request.POST.get('server_url', ''),
                  'server_image': request.POST.get('server_image', '')
                  }
    return result


def trans_user_register(request):
    """
    用于解析前端传送的注册用户的信息
    :param request:
    :return:
    """
    result = {}
    if request.method == 'POST':
        result = {'username': request.POST.get('username', ''),
                  'password': request.POST.get('password', ''),
                  'password_confirmation': request.POST.get('password_confirmation', ''),
                  }
    return result