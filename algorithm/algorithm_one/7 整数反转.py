#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/23/22 3:23 PM 
# @Author : huff 
# @File : 7 整数反转.py 
# @Software: PyCharm

"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
 
示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0
"""

class Solution:
    def reverse(self,x):
        if x < 0:
            temp = str(abs(x))
            re = temp[::-1]
            return -int(re)
        else:
            temp = str(x)
            re = temp[::-1]
            return int(re)


if __name__ == "__main__":
    x = 1534236469
    s = Solution()
    res = s.reverse(x)
    print(res)