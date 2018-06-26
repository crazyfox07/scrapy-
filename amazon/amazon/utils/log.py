# -*- coding:utf-8 -*-
"""
File Name: log
Version:
Description:
Author: liuxuewen
Date: 2018/6/26 10:45
"""
import logging
def get_logger():
    """
    创建日志实例
    """
    logger_ = logging.getLogger(__name__)
    handler = logging.FileHandler(filename='D:\logs\{}.log'.format('amazon2'), mode='w')
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                  datefmt='%a, %d %b %Y %H:%M:%S')
    handler.setFormatter(formatter)
    logger_.addHandler(handler)
    logger_.setLevel(logging.INFO)
    return logger_

logger = get_logger()