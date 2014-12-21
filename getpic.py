#!/usr/bin/python
#coding=utf-8

import requests

n = raw_input('input the school number:')
url = r'http://my.zzti.edu.cn/attachmentDownload.portal?notUseCache=true&type=userFace&ownerId=' + n
headers = {'Cookie': r'*'}

r_get = requests.get(url, headers=headers)
with open("get.jpg", "wb") as code:
     code.write(a.content)
