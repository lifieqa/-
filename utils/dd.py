#!/usr/bin/env python  
# _*_ coding:utf-8 _*_ 
# author :lifie time: 2019/5/25

#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author :lifie time: 2019/5/23

import requests
import json


def getToken():
    url = 'http://api-test.365hdz.com/identity/oauth/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
               'Referer': 'http://dsdgj-pc-test.oss-cn-shanghai.aliyuncs.com/login.html?v=0.7066671286986039'
               }
    data = {
        'username': '18326156509',
        'password': 'ddd111',
        'grant_type': 'password',
        'client_id': '7KKL7bygOnYy',
        'client_secret': '123456'
    }

    r = requests.post(url=url, data=data, headers=headers)
    print(r.text)
    print(r.content)
    print(r.json())
    print(type(r.text))
    print(type(r.content))
    print(type(r.json()))

getToken()