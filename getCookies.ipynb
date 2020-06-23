#微博数据抓取

import time
import pandas as pd
from selenium import webdriver

username="user" #输入你的微博账号
password="pwd"  #输入密码

browser = webdriver.Chrome(r'chromedriver.exe')#通过chromedriver打开浏览器
browser.get('https://s.weibo.com/weibo?q=%E7%8E%8B%E5%87%A4%E9%9B%85&nodup=1')#打开微博界面，可以是任意微博的界面
time.sleep(3)#休眠

#点击登录
browser.find_element_by_xpath('//a[@node-type="loginBtn" and @class="S_txt1"]').click()
time.sleep(3)

browser.find_element_by_xpath("//input[@name='username' and @action-type='text_copy']").send_keys(username)
# 输入微博账号
time.sleep(3)

browser.find_element_by_xpath("//input[@name='password' and @type='password']").send_keys(password)
time.sleep(3)

browser.find_element_by_xpath("//a[@node-type='submitBtn' and @action-type='btn_submit']").click()

time.sleep(50) #在这段时间内接受验证码，并手动输入

cookie_list=browser.get_cookies()#获取cookie
cookie_string='' 
for cookie in cookie_list:#将cookie转换为字符串
    if 'name' in cookie and 'value' in cookie:
        cookie_string += cookie['name'] + '=' + cookie['value'] + ';'


import json
#将获得的cookie保存到txt文件中
jsonCookies = json.dumps(cookie_list)
with open('cookies.txt', 'w') as f:
    f.write(jsonCookies)

#下面这部分测试将cookie输入webdriver中并检验是否成功直接登录
test = webdriver.Chrome(r'chromedriver.exe')#打开浏览器
test.get('https://s.weibo.com/weibo?q=%E7%8E%8B%E5%87%A4%E9%9B%85&xsort=hot&suball=1&Refer=g')#打开微博界面

test.delete_all_cookies()

for cookie in cookie_list:
         #该字段有问题所以删除就可以  浏览器打开后记得刷新页面 有的网页注入cookie后仍需要刷新一下
    if 'expiry' in cookie:
        del cookie['expiry']
    test.add_cookie(cookie)

test.refresh()
time.sleep(5)#休眠

btn = test.find_element_by_xpath("//body[@class='wbs-feed']/div[@class='m-main']/div[@id='pl_"
                                "feed_main']/div[@class='m-wrap']/div[@id='pl_feedlist_index']/div[2]"
                                "/div[@class='card-wrap'][1]/div[@class='card']/div[@class='card-act']/"
                                "ul/li[3]/a")
btn.click()
time.sleep(10)
