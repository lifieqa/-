#!/usr/bin/env python  
# _*_ coding:utf-8 _*_ 
# author :lifie time: 2019/5/22
from utils.public import *
import json
from utils.operationExcel import *

class OperationJson:
    def __init__(self):
        self.excel=OperationExcel()

    def getReadJson(self):
        with open(data_dir(data='data',fileName='requestData.json'), encoding='utf-8') as fp:
            data = json.load(fp)
            return data
    def get_request_data(self,row):
        '''获取请求参数'''
        return json.dumps(self.getReadJson()[self.excel.get_request_data(row)])

# 调试代码
# oper=OperationJson()
# print(oper.get_request_data(1))