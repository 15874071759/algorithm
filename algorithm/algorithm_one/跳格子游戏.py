#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/12/22 11:48 AM 
# @Author : huff 
# @File : 跳格子游戏.py 
# @Software: PyCharm

def solution(n):
    dp = [0 for i in range(n)]
    #print(dp)
    dp[0] =1
    dp[1] =2
    for i in range(2,len(dp)):
        dp[i] = dp[i-1] +dp[i-2]
    count = dp[n-1]
    return count

if __name__ == '__main__':
    n = int(input())
    result = solution(n)
    print(result)



