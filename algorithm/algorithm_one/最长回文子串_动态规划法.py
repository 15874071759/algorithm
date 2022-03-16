#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2/14/22 4:53 PM
# @Author : huff
# @File : 最长回文子串.py
# @Software: PyCharm

"""
给你一个字符串 s，找到 s 中最长的回文子串。
"""

class Solution:
    def longestPalindrome(self, s: str):
        l = len(s)
        if l < 2:
            return s
        dp = [[False for i in range(l)] for i in range(l)]
        for i in range(l):
            dp[i][i] = True
        max_len = 1
        begin = 0
        for Length in range(2,l+1):
            for i in range(l):
                j = i + Length -1
                if j >= l:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    begin = i
        return s[begin:begin+max_len]


if __name__ == "__main__":
    s = "abba"
    #print(s[3:4])
    #result = Solution().isPalindrome(s)
    result = Solution().longestPalindrome(s)
    print(result)
