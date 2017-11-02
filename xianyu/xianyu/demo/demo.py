#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
File Name : 'demo'.py 
Description:
Author: 'zhengyang' 
Date: '2017/6/5' '16:18'
"""

import requests
from xianyu.utils.redis_api import r_proxies


def demo_proxy():

    proxies_str = r_proxies.randomkey()
    if proxies_str:
        ip = proxies_str.split('|')[0]
        port = proxies_str.split('|')[1]
        proxy = {"http": "http://{}:{}".format(ip, port)}

        url = 'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.2.1.ih9JV8&catid=57562002&st_trust=1&q=%CA%D6%EF%ED&ist=1'
        r = requests.get(url)

        print r.text


if __name__ == "__main__":
    demo_proxy()


