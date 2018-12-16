# -*- coding: utf-8 -*-
import hashlib

from django.contrib.auth.hashers import make_password

from login import models


class UserOperation(object):
    """
    用户操作类
    """
    def __init__(self):
        pass

    def add_user(self, receive_data):
        result = {}
        password = receive_data.get('password')
        username = receive_data.get('username')
        user_info = {}
        m = hashlib.md5()
        m.update(password)
        password_new = m.hexdigest()
        user_info['username'] = username
        user_info['password'] = password_new
        try:
            add_result = models.UsersModels.objects.create(**user_info)
            result['username'] = add_result
            result['flag'] = True
        except Exception as e:
            print e.message
            result['flag'] = False
        return result


    def get_all_user(self):
        result = []
        find_result = models.UsersModels.objects.filter()
        for item in find_result:
            user_info = {}
            user_info['username'] = item.username
            user_info['is_active'] = item.is_active
            user_info['is_staff'] = item.is_staff
            user_info['nick_name'] = item.nick_name
            user_info['address'] = item.address
            user_info['age'] = item.age
            user_info['birday'] = item.birday
            user_info['mobile'] = item.mobile
            result.append(user_info)
        return result

    def login_check_user(self, username, password):
        """
        登录校验（自己写的）
        :param username:
        :param password:
        :return:
        """
        result = {}
        # password_new = make_password(password, None, 'pbkdf2_sha256')
        m = hashlib.md5()
        m.update(password)
        password_new = m.hexdigest()
        find_result = models.UsersModels.objects.filter(username=username, password=password_new)
        if find_result:
            result['flag'] = True
        else:
            result['flag'] = False
        return result
