# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UsersModels(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name='昵称')
    birday = models.DateField(verbose_name='生日', null=True, blank=True)
    address = models.CharField(max_length=50, verbose_name='地址', default='')
    mobile = models.CharField(max_length=11, verbose_name='手机', default='')
    sex = models.CharField(max_length=10, default='', verbose_name='性别')
    age = models.CharField(max_length=5, default='', verbose_name='年龄')

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class ServerModels(models.Model):
    id = models.AutoField(primary_key=True, max_length=12)
    server_id = models.IntegerField(null=False, blank=True, verbose_name='服务id', unique=True)
    server_name = models.CharField(max_length=1024, null=False, blank=True, verbose_name='服务名', unique=True)
    server_name_en = models.CharField(max_length=1024, null=False, blank=True, verbose_name='服务英文名')
    server_description = models.CharField(max_length=1024, null=True, blank=True, verbose_name='服务描述信息')
    server_url = models.CharField(max_length=1024, null=False, blank=True, verbose_name='服务跳转url')
    server_token = models.CharField(max_length=24, null=False, blank=True, verbose_name='服务标示')
    server_image = models.CharField(max_length=5000, null=True, blank=True, verbose_name='服务头像数据')

    class Meta:
        db_table = 'server'
        verbose_name = '服务信息'
        verbose_name_plural = verbose_name


class SSOSessionModel(models.Model):
    session_ip = models.CharField(max_length=64, null=False, blank=True, verbose_name='ip', unique=True, primary_key=True)
    session_username = models.CharField(max_length=64, null=True, blank=True, verbose_name='username', unique=False)
    expire_data = models.DateTimeField(max_length=64, null=True, blank=True, verbose_name='expire_time', unique=False)

    class Meta:
        db_table = 'sso_session'
        verbose_name = 'session信息'
        verbose_name_plural = verbose_name