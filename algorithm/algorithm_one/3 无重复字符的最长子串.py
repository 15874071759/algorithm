#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/23/22 11:20 AM 
# @Author : huff 
# @File : 3 无重复字符的最长子串.py 
# @Software: PyCharm

"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        l = len(s)
        if l < 1:
            return 0
        max_len = 1
        for i in range(l):
            if temp.count(s[i]) >= 1:
                index = temp.index(s[i]) #获取子串中重复字符的位置
                temp = temp[index + 1:]
            temp.append(s[i])
            if len(temp) > max_len:
                max_len = len(temp)
        return max_len


if __name__ == "__main__":
    test = "dvdf"
    s = Solution()
    res = s.lengthOfLongestSubstring(test)
    print(res)
