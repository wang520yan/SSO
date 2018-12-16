# -*- coding: utf-8 -*-
import random


def get_random_str(num, type=None):
    """
    获得指定长度的随机字符串
    :param num: 字符串长度
    :param type: 想要的字符串类型，ps：upper(大写），lower（小写), number(数字），upnum(大写加数字），lownum（小写加数字），uplow（大写加小写），uplownum（大写加小写加数字）默认为uplownum
    :return:
    """
    random_str = ''
    if type == 'upper':
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif type == 'lower':
        chars = 'abcdefghijklmnopqrstuvwxyz'
    elif type == 'number':
        chars = '1234567890'
    elif type == 'upnum':
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    elif type == 'lownum':
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    elif type == 'uplow':
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    else:
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    length = len(chars)
    if num:
        for ik in range(num):
            random_str += chars[random.randint(0, length-1)]
    return random_str


if __name__ == '__main__':
    get_random_str(10, 'uplow')

