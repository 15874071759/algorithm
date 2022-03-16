#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/11/22 9:47 PM 
# @Author : huff 
# @File : 漂流船问题.py 
# @Software: PyCharm

def solution(weight, load):
    weight.sort(reverse=True)
    #print(weight)
    result = 0
    i = 0
    j = len(weight)-1
    while i <= j:
        if int(weight[i]) + int(weight[j]) <= int(load):
        #if weight[i] + weight[j] <= load:
            i +=1
            j -=1
        else:
            i +=1
        result +=1
    return result


if __name__ == "__main__":
    weight = input().split(" ")
    load = input()
    re = solution(weight, load)
    print(re)




