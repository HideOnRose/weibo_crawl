# weibo_crawl
### 1.获取并保存cookies
getCookies文件使用selenium包中的webdriver工具打开网页<br>
模拟点击和账号密码的输入后<br>
获取cookies并保存到文件中<br>

在登陆账号后，微博有可能会要求进行验证，通过time.sleep（50）来给予充分的时间进行验证<br>

### 2.使用scrapy框架爬取微博内容
scrapy框架架构大体如下：
![] (https://raw.githubusercontent.com/HideOnRose/weibo_crawl/master/img/scrapy.jpg)

在中间件中使用selenium，读取之前保存的cookies即可实现直接登录<br>

在spider中定位界面元素时 推荐使用xpath，其语法为:<br>
元素[@属性='' and @元素='']/元素[@..]<br>
使用/表示选择该节点下的一级子元素，使用//选择该节点下的所有子元素<br>






