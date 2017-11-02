# -*- coding:utf-8 -*-

"""
File Name : 'distinct'.py
Description:
Author: 'chengwei'
Date: '2016/6/2' '11:45'
"""

from Configs import RedisParms
import sys
import hashlib
import redis

reload(sys)
sys.setdefaultencoding('utf-8')

"""
利用redis的集合不允许添加重复元素来进行去重
"""


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


def redis_init(parasecname="Redis"):
    u"""
    初始化redis
    :param parasecname:
    :return: redis连接池
    """
    # redis
    pool = redis.ConnectionPool(host=RedisParms.server, port=6379, db=0, password=RedisParms.passwd)
    r = redis.Redis(connection_pool=pool)

    return pool, r


def sha1(x):
    sha1obj = hashlib.sha1()
    sha1obj.update(x)
    hash_value = sha1obj.hexdigest()
    return hash_value


def check_repeate(r, check_str, set_name):
    u"""
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
    u"""
    释放redis连接池
    :param pool:
    :return:
    """
    pool.disconnect()

if __name__ == '__main__':
    example()
