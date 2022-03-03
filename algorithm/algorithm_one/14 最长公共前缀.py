#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 3/3/22 5:48 PM 
# @Author : huff 
# @File : 14 最长公共前缀.py 
# @Software: PyCharm

"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
"""
class Solution:
    def longestCommonPrefix(self,strs):
        max_pre = strs[0]
        l = len(strs)
        for i in range(1, l):
            j = 0
            while j< len(max_pre) and j < len(strs[i]) and max_pre[j] == strs[i][j]:
                j += 1
                #max_index = j
            max_pre = strs[0][0:j]
        return max_pre


if __name__ == "__main__":
    s = Solution()
    #strs = ["flower","flow","flight"]
    strs = ["dog", "racecar", "car"]
    re = s.longestCommonPrefix(strs)
    print(re)