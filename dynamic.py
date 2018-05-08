#!/usr/bin/env python
#coding:utf-8

import sys
import time
import hashlib
import requests
from lxml import etree
from bs4 import BeautifulSoup as BS
import random

def dynamic(url):
    _version = sys.version_info

    is_python3 = (_version[0] == 3 )

    orderno = "ZF20183171164keG5GQ"           # 订单号
    secret = "2d045b80694b447990b0688c43c96c59"        # 账户管理里面的sercet码

    #接入ip和端口
    ip = "forward.xdaili.cn"

    port = "80"

    ip_port = ip + ":" + port

    timestamp = str(int(time.time()))     # 计算时间戳
    string = ""
    string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

    if is_python3:
        string = string.encode()

    md5_string =hashlib.md5(string).hexdigest()  #计算sign
    sign = md5_string.upper()
    #print(sign)

    auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
    #print(auth)

    proxy = {"http" : "http://" + ip_port, "https" : "http://" + ip_port}

    user_agent = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50']

    headers = {"Proxy-Authorization" : auth,
               "user-agent" : "{}".format(random.choice(user_agent)),
               "referer" : url,
               }

    r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False,timeout=180)
    if r.status_code == 302 or r.status_code == 301 or r.status_code == 307:
        loc = r.headers['Location']
        url_f = loc
        r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False,time=180)
        if r.status_code == 302 or r.status_code == 301 or r.status_code == 307:
            loc = r.headers['location']
            url_f = loc
            r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False,time=180)

    return r