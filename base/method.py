#!/usr/bin/env python  
# _*_ coding:utf-8 _*_ 
# author :lifie time: 2019/5/22

import requests
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationJson import  OperationJson
from page.pro import *


class  Method:
    def __init__(self):
        self.operationJson = OperationJson()
        self.excel = OperationExcel()

    def post_yuanshi(self, row):
        '''最原始的post封装'''
        try:
            r = requests.post(
                url=self.excel.getUrl(row=row),
                data=self.operationJson.get_request_data(row=row),
                headers=getHeadersValues(),
                timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')
    def post_update(self, row,data):
        '''请求数据重新修改后，调用的post方法'''
        try:
            r = requests.post(
                url=self.excel.getUrl(row=row),
                data=data,
                headers=getHeadersValues(),
                timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')
    def put(self,row):
        r=requests.put(url=getUrls(row=row),
                       data=self.operationJson.get_request_data(row=row),
                       headers=getHeadersValues()
                       )
        return r
    def delete(self,row):
        r=requests.delete(url=getUrls(row=row),
                          headers=getHeadersValues())
        return r
class IsContent:
    def __init__(self):
        self.excel=OperationExcel()

    def isContent(self,row,str2):
        flag=None
        if self.excel.getExpect(row) in str2:
            flag= True
        else:
            flag =False
        return flag

