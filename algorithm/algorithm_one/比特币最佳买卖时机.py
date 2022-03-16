#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/12/22 8:04 PM 
# @Author : huff 
# @File : 比特币最佳买卖时机.py 
# @Software: PyCharm

def solution(list):
    max_temp = 0
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            temp = int(list[j])-int(list[i])
            if temp > max_temp:
                max_temp = temp
    return max_temp


if __name__ == "__main__":
    #list = [7,1,5,3,6,4]
    list = input().split(" ")
    #print(list)
    result = solution(list)
    print(result)


        