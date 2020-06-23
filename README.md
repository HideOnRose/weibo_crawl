# weibo_crawl
###1.获取并保存cookies<br>
getCookies文件使用selenium包中的webdriver工具打开网页<br>
模拟点击和账号密码的输入后<br>
获取cookies并保存到文件中<br>

在登陆账号后，微博有可能会要求进行验证，通过time.sleep（50）来给予充分的时间进行验证<br>

###2.使用scrapy框架爬取微博内容<br>



