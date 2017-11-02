# -*- coding: utf-8 -*-

# Scrapy settings for xianyu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xianyu'

SPIDER_MODULES = ['xianyu.spiders']
NEWSPIDER_MODULE = 'xianyu.spiders'

#重试设置
RETRY_ENABLED = True
RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

REDIS_HOST = "99.48.58.244"
REDIS_PWD = "mime@123"
REDIS_DB_PROXIES = 6
REDIS_DB_DISTINCT = 3
REDIS_PORT = 6379
REDIS_SET_NAME = '{}:task_remove_repeate'.format(BOT_NAME)

MYSQL_HOST = '115.29.177.124'
MYSQL_DBNAME = 'CRAWL_DB'
MYSQL_USER = 'nj.crawl'
MYSQL_PASSWD = 'nj.crawl'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENTS =  [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#日志
# LOG_ENABLED = False
import platform
if platform.system() == 'Windows':
    LOG_FILE = r'D:\logs\{}.log'.format(BOT_NAME)
else:
    LOG_FILE = '/usr/local/log/{0}.log'.format(BOT_NAME)


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xianyu (+http://www.yourdomain.com)'


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 11
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 5
CONCURRENT_REQUESTS_PER_IP = 5

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'Host':'2.taobao.com',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#'Referer':'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.9fhcHT&catid=50456012&st_trust=1&page=3&ist=1',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cookie':'swfstore=268758; mt=ci%3D-1_0; thw=cn; miid=1320244093702563224; UM_distinctid=15c5db35aff3f7-02aa7bd173c42c-4e47052e-1fa400-15c5db35b006d3; t=81b8eab296fcc461a58482ae5c886889; _cc_=WqG3DMC9EA%3D%3D; tg=0; l=AiwseJWuC82tSIDf-h0x6KLEfAFeItCP; cookie2=3c878e2b010e38fa066e2258b6b4ea6c; _tb_token_=eaebb487b5843; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; mt=ci=0_0; v=0; CNZZDATA1252911424=1552399349-1496216626-https%253A%252F%252F2.taobao.com%252F%7C1496294854; CNZZDATA30058275=cnzz_eid%3D1246761729-1496217851-https%253A%252F%252F2.taobao.com%252F%26ntime%3D1496292873; cna=lGyAEZVnAjQCAd3iVZIEIqo4; isg=AsvLHrc0Fr3noUpEzinBzo21Wm_WUOXuzWhv1j3Ij4phXOu-xTBvMmk-QmpJ'
}
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#'Cookie':'thw=cn; l=Atzcb31Xu92d2FCvqo1BvsB7LPGOL4B/; miid=1320244093702563224; t=81b8eab296fcc461a58482ae5c886889; v=0; cookie2=1c039a064b6a91c70f022b533132dc85; _tb_token_=efe81e6eb8f3b; UM_distinctid=15c5db35aff3f7-02aa7bd173c42c-4e47052e-1fa400-15c5db35b006d3; CNZZDATA30057895=cnzz_eid%3D1476408017-1496217529-%26ntime%3D1496217529; mt=ci%3D-1_0; CNZZDATA30058279=cnzz_eid%3D989154842-1496220169-%26ntime%3D1496279570; CNZZDATA1252911424=1323606497-1496216626-%7C1496278654; cna=lGyAEZVnAjQCAd3iVZIEIqo4; isg=Ao6OVUc1W9b_7O_fC5Z89aCy32QzP2gF8M_KrbjXaBFMGyx1IJ0lGKUZJ3GM',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xianyu.middlewares.XianyuSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'xianyu.middlewares.BlankPageRetryMiddleware':20,
  'xianyu.middlewares.RandomUserAgent': 100,
   'xianyu.middlewares.XianyuSpiderMiddleware': 543,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xianyu.pipelines.XianyuPipeline': 300,
   'xianyu.pipelines.MySQLStorePipeline': 500,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
