#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：计算字符串中某字符串出现的次数。
'''

if __name__ == '__main__':
    str1 = raw_input('input a string:\n')
    str2 = raw_input('input a sub string:\n')
    ncount = str1.count(str2)
    print ncount