

import random


def get_proxies():


    proxies_list = [
        {"http": "http://54.222.232.0:3128", "https": "http://54.222.232.0:3128"},
        {"http": "http://54.222.248.157:3128", "https": "http://54.222.248.157:3128"},
        {"http": "http://54.222.206.125:3128", "https": "http://54.222.206.125:3128"},
        {"http": "http://54.222.234.209:3128", "https": "http://54.222.234.209:3128"},
        {"http": "http://54.223.161.39:3128", "https": "http://54.223.161.39:3128"},
        {"http": "http://54.223.156.59:3128", "https": "http://54.223.156.59:3128"},
        {"http": "http://54.223.159.148:3128", "https": "http://54.223.159.148:3128"},
        {"http": "http://54.223.21.123:3128", "https": "http://54.223.21.123:3128"},
        {"http": "http://54.222.168.162:3128", "https": "http://54.222.168.162:3128"},
        {"http": "http://54.223.33.4:3128", "https": "http://54.223.33.4:3128"},
        {"http": "http://54.223.94.4:3128", "https": "http://54.223.94.4:3128"},
        {"http": "http://54.222.198.175:3128", "https": "http://54.222.198.175:3128"},
        {"http": "http://52.80.30.13:3128", "https": "http://52.80.30.13:3128"},
        {"http": "http://52.80.40.255:3128", "https": "http://52.80.40.255:3128"},
        {"http": "http://54.222.241.163:3128", "https": "http://54.222.241.163:3128"},
        {"http": "http://52.80.11.103:3128", "https": "http://52.80.11.103:3128"},
        {"http": "http://52.80.28.179:3128", "https": "http://52.80.28.179:3128"},
        {"http": "http://52.80.34.136:3128", "https": "http://52.80.34.136:3128"},
        {"http": "http://54.223.198.168:3128", "https": "http://54.223.198.168:3128"},
        {"http": "http://52.80.44.176:3128", "https": "http://52.80.44.176:3128"},
        {"http": "http://52.80.45.166:3128", "https": "http://52.80.45.166:3128"},
        {"http": "http://52.80.38.37:3128", "https": "http://52.80.38.37:3128"}
    ]

    return random.choice(proxies_list)
