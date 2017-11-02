#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
File Name : 'tools'.py 
Description:
Author: 'zhengyang' 
Date: '2017/5/24' '18:07'
"""

import hashlib
import re
import sys


from xianyu.utils.redis_api import r_distinct, redis_set_name

reload(sys)
sys.setdefaultencoding('utf-8')



def remove_hash_url(hash_value):
    r_distinct.srem(redis_set_name,hash_value)


def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value		# Instance of unicode


def to_str(unicode_or_str):
    if isinstance(unicode_or_str,	unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value		# Instance of	str


def is_in(hash_value,r=r_distinct, set_name=redis_set_name):
    result = r.sismember(set_name,hash_value)
    return result


def add_url_hash(hash_value, r=r_distinct, set_name=redis_set_name):
    r.sadd(set_name, hash_value)


def is_new(hash_value, r=r_distinct, set_name=redis_set_name):
    """
    向redis集合中添加元素，重复则返回0，不重复则添加成功，并返回1
    :param r:redis连接
    :param hash_value:被添加的字符串
    :param set_name:项目所使用的集合名称，建议如下格式：”projectname:task_remove_repeate“
    :return: is new: 1  not is new: 0
    """
    result = r.sadd(set_name, hash_value)
    return result


def get_hash(raw_str):
    """
    对item的内容做hash 返回字符串的hash值
    先做sha1 再对10 ** 12 取模
    :param raw_str:
    :return:
    """
    sha1obj = hashlib.sha1()
    sha1obj.update(raw_str)
    return int(sha1obj.hexdigest(), 16) % (10 ** 12)


















