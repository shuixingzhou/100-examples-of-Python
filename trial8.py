#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
9*9乘法口诀
'''

for i in range(1, 10):
    print 
    for j in range(1, i+1):
        print "%d*%d=%d" % (i, j, i*j)
