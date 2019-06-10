#!/usr/bin/env python  
# _*_ coding:utf-8 _*_ 
# author :lifie time: 2019/5/28

import unittest
import os
import HTMLTestRunner
import time

def getSuite():
    '''获取测试套件'''
    suite = unittest.TestLoader().discover(
        start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests'),
        pattern='test_*.py',
        top_level_dir=None)
    return suite
def getNowtime():
    '''获取当前时间戳'''
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))


def run():
    fp =os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report',getNowtime()+ 'testReport.html')
    HTMLTestRunner.HTMLTestRunner(stream=open(fp, 'wb'),
                                  title='自动化测试报告',
                                  description='自动化测试报告详细信息').run(getSuite())

if __name__ == '__main__':
    run()