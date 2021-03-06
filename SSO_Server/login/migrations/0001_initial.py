# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-15 16:39
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nick_name', models.CharField(max_length=20, verbose_name='\u6635\u79f0')),
                ('birday', models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5')),
                ('address', models.CharField(default='', max_length=50, verbose_name='\u5730\u5740')),
                ('mobile', models.CharField(default='', max_length=11, verbose_name='\u624b\u673a')),
                ('sex', models.CharField(default='', max_length=10, verbose_name='\u6027\u522b')),
                ('age', models.CharField(default='', max_length=5, verbose_name='\u5e74\u9f84')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ServerModels',
            fields=[
                ('id', models.AutoField(max_length=12, primary_key=True, serialize=False)),
                ('server_id', models.IntegerField(blank=True, unique=True, verbose_name='\u670d\u52a1id')),
                ('server_name', models.CharField(blank=True, max_length=1024, unique=True, verbose_name='\u670d\u52a1\u540d')),
                ('server_name_en', models.CharField(blank=True, max_length=1024, verbose_name='\u670d\u52a1\u82f1\u6587\u540d')),
                ('server_description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='\u670d\u52a1\u63cf\u8ff0\u4fe1\u606f')),
                ('server_url', models.CharField(blank=True, max_length=1024, verbose_name='\u670d\u52a1\u8df3\u8f6curl')),
                ('server_token', models.CharField(blank=True, max_length=24, verbose_name='\u670d\u52a1\u6807\u793a')),
                ('server_image', models.CharField(blank=True, max_length=5000, null=True, verbose_name='\u670d\u52a1\u5934\u50cf\u6570\u636e')),
            ],
            options={
                'db_table': 'server',
                'verbose_name': '\u670d\u52a1\u4fe1\u606f',
                'verbose_name_plural': '\u670d\u52a1\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='SSOSessionModel',
            fields=[
                ('session_ip', models.CharField(blank=True, max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='ip')),
                ('session_username', models.CharField(blank=True, max_length=64, null=True, verbose_name='username')),
                ('expire_data', models.DateTimeField(blank=True, max_length=64, null=True, verbose_name='expire_time')),
            ],
            options={
                'db_table': 'sso_session',
                'verbose_name': 'session\u4fe1\u606f',
                'verbose_name_plural': 'session\u4fe1\u606f',
            },
        ),
    ]
