#!/usr/bin/env python  
# _*_ coding:utf-8 _*_ 
# author :lifie time: 2019/5/22

from utils.getnewtoken import *


class ExcelVariable:
    caseID = 0
    url = 2
    request_data = 3
    expect = 4
    result = 5


def getCaseID():
    return ExcelVariable.caseID


def getUrl():
    return ExcelVariable.url


def get_request_data():
    return ExcelVariable.request_data


def getExpect():
    return ExcelVariable.expect


def getResult():
    return ExcelVariable.result


def getHeadersValue():
    '''获取请求头,这个是写死的请求头'''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'bearer 68717bbd-de26-44d8-bb2f-cfefffa40624',
    }
    return headers



def getHeadersValues():
    '''每次登陆获取最新的token，修改请求头'''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': None
    }
    headers['Authorization'] = getToken()
    return headers


getHeadersValues()
