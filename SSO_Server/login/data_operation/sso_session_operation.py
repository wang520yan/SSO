# -*- coding: utf-8 -*-
import base64
import hashlib
import time

from login import models


class SSOSessionOperation(object):
    """
    单点登录session
    """
    def __init__(self):
        pass

    def add_session(self, receive_data):
        """
        增加session
        :param receive_data:
        :return:
        """
        session_info = {}
        ip = receive_data.get('session_ip')
        session_ip = base64.b64encode(bytes(ip))
        session_info['session_ip'] = session_ip
        # base64.b64decode(base64.b64encode(bytes(s, 'ascii')))
        username = receive_data.get('session_username')
        session_username = base64.b64encode(bytes(username))
        session_info['session_username'] = session_username
        time_now = int(time.time())
        expire_time = time_now + 60 * 30
        timeArray = time.localtime(expire_time)
        expire_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        session_info['expire_data'] = expire_time
        models.SSOSessionModel.objects.create(**session_info)

    def delete_session(self, ip):
        """
        删除session
        :param ip:
        :return:
        """
        session_ip = base64.b64encode(bytes(ip))
        models.SSOSessionModel.objects.filter(session_ip=session_ip).delete()

    def check_login_by_ip(self, ip):
        """
        通过ip为标志校验登录
        :param ip:
        :return:
        """
        username_new = ''
        session_ip = base64.b64encode(bytes(ip))
        find_result = models.SSOSessionModel.objects.filter(session_ip=session_ip)
        if find_result:
            for item in find_result:
                username = item.session_username
                username_new = base64.b64decode(bytes(username))
        return username_new

    def check_session_expire_time(self):
        """
        校验登录的session是否过期
        :return:
        """
        find_result = models.SSOSessionModel.objects.filter()
        if find_result:
            for item in find_result:
                ip = item.session_ip
                expire_time = item.expire_data
                timeArray = time.strptime(expire_time, "%Y-%m-%d %H:%M:%S")
                expire_timeStamp = int(time.mktime(timeArray))
                time_now = int(time.time())
                all_time = time_now - expire_timeStamp
                if all_time > 0:
                    models.SSOSessionModel.objects.filter(session_ip=ip).delete()
                else:
                    continue

