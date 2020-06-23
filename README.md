# weibo_crawl
### 1.获取并保存cookies
getCookies文件使用selenium包中的webdriver工具打开网页<br>
模拟点击和账号密码的输入后<br>
获取cookies并保存到文件中<br>

在登陆账号后，微博有可能会要求进行验证，通过time.sleep（50）来给予充分的时间进行验证<br>

### 2.使用scrapy框架爬取微博内容
scrapy框架架构大体如下：<br>
* 由引擎将start_requests交给调度器，将requests请求排序入队。
* 调度器将处理好的request交给引擎
* 引擎将request交给下载器，由下载器请求该request生成响应response，然后将response返回给引擎
* 引擎将生成的response交给spider，在spider中对响应中的数据进行提取
* spider将提取到的数据交给管道，管道对数据进行保存处理，如果是需要跟进的url，则交给调度器将该url生成request
* 当调度器中不存在任何request了，整个程序才会停止，也就是说对于下载失败的url，scrapy也会重新下载


因此要实现登录和提前点击，是在下载中间件中使用selenium，读取之前保存的cookies即可实现直接登录<br>

在spider中定位界面元素时 推荐使用xpath，其语法为:<br>
元素[@属性='' and @元素='']/元素[@..]<br>
使用/表示选择该节点下的一级子元素，使用//选择该节点下的所有子元素<br>

一些出现的问题：
* cookies每隔一段时间就会失效，需要重新获取
* 在selenium中，如果是要找元素组，应该是find_elements_by_xpath, find_element_by找到的是单个元素,无法遍历
* 微博的内容有一些需要展开全文，展开和无展开的内容中 元素的class有所不同，需要注意








