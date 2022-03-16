#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-05-18 00:29 
# @Author : huff 
# @File : 最长子串.py 
# @Software: PyCharm

alist = [5,6,3,8,1]
#blist = [1,1,1,1,1]
blist = []

for i in range(len(alist)):
    blist.append(1)
    for j in range(i):
        if alist[i] > alist[j]:
            blist[i] = max(blist[i], blist[j]+1)
print(blist)
print(max(blist))