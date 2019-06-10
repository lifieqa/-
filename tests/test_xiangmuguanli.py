#!/usr/bin/env python  
# _*_ coding:utf-8 _*_ 
# author :lifie time: 2019/5/22

import unittest
import json
from base.method import Method, IsContent
from page.pro import *
from utils.operationExcel import OperationExcel


class Xiangmuguanli(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = IsContent()
        self.opexcel=OperationExcel()

    def statusCode(self, r):
        self.assertEqual(r.status_code, 200)

    def isContent(self, r, row):
        self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=row, str2=r.text))

    def test_001_insert(self):
        '''项目管理：新增测试'''
        r = self.obj.post_yuanshi(row=1)
        # self.statusCode(r=r)
        # self.assertTrue(self.p.isContent(row=1,str2=r.text))
        # 上面两句断言封装一个方法
        self.isContent(r=r, row=1)
        # 把结果写到表格里
        self.opexcel.writeResult(row=1,content='pass')



        # print(r.text)

    # def test_001_insert_updatename(self):
    #     '''项目管理：请求数据的重新赋值'''
    #     r = self.obj.post_update(row=1, data=updateData(name='电风扇'))
    #     self.isContent(r=r, row=1)

    # def test_002_chaxun_str(self):
    #     r = self.obj.post_yuanshi(2)
    #     self.isContent(r=r, row=2)
    #     for i in range(0, 10):
    #         if r.json()['data'][i]['name'] == '搜索':
    #             id = r.json()['data'][i]['id']
    #     writePositionId(id)

    def test_002_chaxun_list(self):
        '''项目管理：查询测试'''
        list1 = []
        r = self.obj.post_yuanshi(2)
        self.isContent(r=r, row=2)
        for i in range(0, 10):
            if r.json()['data'][i]['name'] == '搜索':
                id = r.json()['data'][i]['id']
                list1.append(id)
                # print(list1)
                # print(type(list1))
        writePositionId(json.dumps(list1))

    def test_003_upate(self):
        '''项目管理：修改测试'''
        r=self.obj.put(row=3)
        print(r.url)
        self.isContent(r=r,row=3)

    def test_004_delete(self):
        '''项目管理：删除测试'''
        r=self.obj.delete(row=4)
        self.isContent(r=r,row=4)
        # print(r.url)
if __name__ == '__main__':
    unittest.main(verbosity=2)
