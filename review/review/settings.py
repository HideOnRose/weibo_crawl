# -*- coding: utf-8 -*-

# Scrapy settings for review project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'review'

SPIDER_MODULES = ['review.spiders']
NEWSPIDER_MODULE = 'review.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'review (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',

    'Cookie': 'SINAGLOBAL=3135417824870.461.1585026656690; SCF=AmWNjvCo_lSlu23sIdfE5n0kI4mhn_20k_SQ' \
              'GRN7KU7P5wRLrov20GjI6PV2luNS2v50Ku7UMcWKUm9hhMF58RU.; SUHB=0WGsWv5FGWoe3C; SUBP=0033WrSXq' \
              'PxfM725Ws9jqgMF55529P9D9Wh-n.lFRJGamR1eocv1fYG75JpX5oz75NHD95Qceon01he0SoM0Ws4DqcjZCsL.9-' \
              'vV-Jv09Btt; ALF=1588588678; SUB=_2A25zjBPVDeRhGeBM41EZ8y3KzD-IHXVQjr2drDV8PUJbkNAfLXGmkW1N' \
              'RKl5nE4h1trvd0BxU36bvLhL1ojp-NMD; wvr=6; UOR=www.cnblogs.com,widget.weibo.com,www.baidu.co' \
              'm; _s_tentry=-; Apache=4485081821265.022.1587365212153; ULV=1587365212159:7:6:1:448508182126' \
              '5.022.1587365212153:1586882741767; webim_unReadCount=%7B%22time%22%3A1587365363194%2C%22d' \
              'm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allco' \
              'untNum%22%3A7%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/81.0.4044.113 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'review.middlewares.ReviewSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
   'review.middlewares.SeleniumMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
   'review.pipelines.ReviewPipeline': 572,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
