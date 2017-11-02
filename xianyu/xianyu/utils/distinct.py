# -*- coding:utf-8 -*-

"""
File Name : 'distinct'.py
Description: 利用redis的集合不允许添加重复元素来进行去重
Author: 'chengwei'
Date: '2016/6/2' '11:45'
"""

import sys
import hashlib
import os
import codecs
import redis



reload(sys)
sys.setdefaultencoding('utf-8')


def sha1(x):
    sha1obj = hashlib.sha1()
    sha1obj.update(x)
    hash_value = sha1obj.hexdigest()
    return hash_value


def check_repeate(r, check_str, set_name):
    """
    向redis集合中添加元素，重复则返回0，不重复则添加成功，并返回1
    :param r:redis连接
    :param check_str:被添加的字符串
    :param set_name:项目所使用的集合名称，建议如下格式：”projectname:task_remove_repeate“
    :return:
    """
    hash_value = sha1(check_str)
    result = r.sadd(set_name, hash_value)
    return result


def redis_close(pool):
    """
    释放redis连接池
    :param pool:
    :return:
    """
    pool.disconnect()




