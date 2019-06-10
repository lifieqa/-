#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# author :lifie time: 2019/5/23

from utils.operationJson import OperationJson
from utils.operationExcel import OperationExcel
import json
from utils.public import *
import chardet

opjson = OperationJson()
opexcel=OperationExcel()


def updateData(name=None):
    dict1 = json.loads(opjson.get_request_data(1))
    dict1['name'] = name
    return json.dumps(dict1)


def writePositionId(content):
    '''把新增的项目对应的ID写到data文件夹下的xiangmuID文件中'''
    with open(data_dir(data='data', fileName='xiangmuID'), 'w') as f:
        f.write(content)


def getPositionId():
    '''获取xiangmuID文件中的ID'''
    with open(data_dir(data='data', fileName='xiangmuID'), 'r') as f:
        return json.loads(f.read())
# def getUrl():
#     urlnew='http://api-test.365hdz.com/basic/services/{0}'.format(getPositionId()[0])
#     return urlnew
def getUrls(row):
    '''根据行获取地址，然后对地址进行格式化输入关联项目ID'''
    urlnew=opexcel.getUrl(row=row)
    urlnews=urlnew+'{0}'.format(getPositionId()[0])
    return urlnews


# 调用代码
# getUrls(row=3)
# updateData('电风扇')
