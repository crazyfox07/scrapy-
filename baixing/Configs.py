#! /usr/bin/env python
# -*- coding: utf-8 -*-

u"""
---------------------------------------------------------------
File Name: Configs.py
Version : 0.1
Description: 将需要使用配置信息定义在该文件中

Author  : gonghao
Date    : 2016-06-14 16:12:17
---------------------------------------------------------------
"""


class RabbitMQ(object):
    u"""
    定义 RabbitMQ 的参数
    """
    host = "99.48.58.244"
    username = "admin"
    passwd = "12345"


class DBParms(object):
    u"""
    定义不同数据库的参数
    """
    admin = ('99.48.58.208', 'sa', 'mime@123')


class RedisParms(object):
    u"""
    定义　Redis 参数
    """
    server = "99.48.58.244"
    passwd = "mime@123"
