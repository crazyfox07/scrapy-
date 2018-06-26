# -*- coding:utf-8 -*-
"""
File Name: proxies
Version:
Description:
Author: liuxuewen
Date: 2018/6/26 10:22
"""
import itertools
import random
import redis

pool = redis.ConnectionPool(host='99.48.58.244', port=6379, db=13, password='mime@123')
r = redis.StrictRedis(connection_pool=pool)

def get_aws_proxies():
    """
    随机返回一个*aws*代理ip(aws ec2上squid设置) 适用于对爬取质量要求高的网站
    :return:
    """

    ip_list_1 = ['54.222.232.0', '54.222.198.175', '54.222.248.157', '54.222.206.125',
                 '54.222.234.209', '54.223.161.39', '54.223.156.59', '54.223.159.148',
                 '54.223.21.123', '54.222.168.162', '54.223.33.4', '54.223.94.4',
                 ]

    ip_list_2 = ['52.80.79.173', '54.222.203.11', '54.222.205.72', '52.80.83.243',
                 '54.222.241.163', '52.80.11.103', '52.80.28.179', '52.80.34.136',
                 '54.223.198.168', '52.80.44.176', '52.80.45.166', '52.80.38.37'
                 ]

    ip_list_3 = ['52.80.61.73', '52.80.40.255', '52.80.41.23', '52.80.52.24',
                 '52.80.88.180', '52.80.26.246', '52.80.73.35', '52.80.89.0']

    http_str = 'http://{}:3128'

    https_str = 'https://{}:3128'

    proxies_list = [dict(http=http_str.format(ip), https=https_str.format(ip))
                    for ip in itertools.chain(ip_list_1, ip_list_2, ip_list_3)]

    return random.choice(proxies_list)


def get_proxy_from_redis():
    items = [key.decode(encoding='utf8').split('|') for key in r.keys()]
    item = random.choice(items)
    host, port = item[0].split(':')[1], item[1]
    proxy = {
        'http':'http://{}:{}'.format(host,port),
        'https': 'https://{}:{}'.format(host, port)
    }
    return proxy


if __name__ == '__main__':
    get_proxy_from_redis()
