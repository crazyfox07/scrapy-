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
config = get_config()


reload(sys)
sys.setdefaultencoding('utf-8')


def example():
    pool, r = redis_init()
    temp_str = "aaaaaaaaa"
    result = check_repeate(r, temp_str, 'test:test')
    if result == 0:
        # do what you want to do
        print u"重复"
    else:
        # do what you want to do
        print u"不重复"
    redis_close(pool)


def redis_init():
    """
    初始化redis
    :param parasecname:
    :return: redis连接池
    """

    redis_host = config.REDIS_HOST
    redis_pass = config.REDIS_PWD
    redis_db = config.REDIS_DB
    redis_port = config.REDIS_PORT

    # redis
    pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=redis_db, password=redis_pass)
    # r = redis.Redis(connection_pool=pool)
    r = redis.StrictRedis(connection_pool=pool)

    return pool, r


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


def is_repeat(check_str, set_name):
    """
    检查是否重复
    :param check_str:
    :param set_name:
    :return:
    """
    pool, r = redis_init()
    result = check_repeate(r, check_str, set_name)
    if result == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print is_repeat("aaaa", "merchant:risk")