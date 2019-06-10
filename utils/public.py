#!/usr/bin/env python  
# _*_ coding:utf-8 _*_ 
# author :lifie time: 2019/5/22

import os

def data_dir(data=None,fileName=None):
    '''查找文件的路径'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)

#调试代码
# print(data_dir(data='data',fileName='data.xls'))
