#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-25 11:43 
# @Author : huff 
# @File : 69 x的平方根.py 
# @Software: PyCharm
'''
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left,right = 1, x//2
        while left < right:
            mid = left + (right - left+1)//2
            if x/mid < mid:
                right = mid-1
            else:
                left = mid
        return left

if __name__ == '__main__':
    x = 1024
    s = Solution()
    result = s.mySqrt(x)
    print('平方根',result)