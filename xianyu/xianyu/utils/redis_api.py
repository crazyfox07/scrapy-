#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
File Name : 'redis_api'.py 
Description:
Author: 'zhengyang' 
Date: '2017/3/7' '15:43'
"""
import redis
from xianyu.settings import REDIS_HOST, REDIS_PWD, REDIS_DB_PROXIES, REDIS_DB_DISTINCT, REDIS_PORT, REDIS_SET_NAME


user = REDIS_HOST
password = REDIS_PWD
host = REDIS_HOST
db_proxies = REDIS_DB_PROXIES
db_distinct = REDIS_DB_DISTINCT
port = REDIS_PORT
redis_set_name = REDIS_SET_NAME

pool_6 = redis.ConnectionPool(host=host, port=port, db=db_proxies, password=password)
r_proxies = redis.StrictRedis(connection_pool=pool_6)

pool_7 = redis.ConnectionPool(host=host, port=port, db=db_distinct, password=password)
r_distinct = redis.StrictRedis(connection_pool=pool_7)


if __name__ == "__main__":
    # print is_new(123456)
    pass








