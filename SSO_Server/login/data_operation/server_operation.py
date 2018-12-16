# -*- coding: utf-8 -*-
import random
import time

from login import models
from login.get_random_data import get_random_str


class ServerOperation(object):
    """
    服务相关操作类
    """
    def __init__(self):
        pass

    def add_server(self, receive_data):
        """
        注册服务信息入库
        :param receive_data:
        :return:
        """
        result = {}
        # receive_data = {'server_name': '任务管理',
        #           'server_name_en': 'task',
        #           'server_description': '协同式任务管理系统',
        #           'server_url': 'http://192.168.1.102:7006/login',
        #           'server_image': ''
        #           }
        server_id = int(time.time()) + random.randint(0, 100)
        receive_data['server_id'] = server_id
        token = get_random_str(10, 'upper')
        receive_data['server_token'] = token
        print receive_data
        save_result = models.ServerModels.objects.create(**receive_data)
        result['token'] = token
        return result

    def get_all_servers(self):
        """
        获取所有的服务信息
        :return:
        """
        result = []
        find_result = models.ServerModels.objects.filter()
        for item in find_result:
            server_info = {}
            server_info['server_id'] = item.server_id
            server_info['server_name'] = item.server_name
            server_info['server_name_en'] = item.server_name_en
            server_info['server_description'] = item.server_description
            server_info['server_url'] = item.server_url
            server_info['server_image'] = item.server_image
            result.append(server_info)
        return result

    def check_login_by_token(self, token):
        """
        根据token校验请求是否正确
        :param token:
        :return:
        """
        result = {}
        find_result = models.ServerModels.objects.filter(server_token=token)
        if find_result:
            result['flag'] = True
        else:
            result['flag'] = False
        return result


if __name__ == '__main__':
    pass
