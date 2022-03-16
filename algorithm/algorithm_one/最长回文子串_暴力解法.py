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
    def isPalindrome(self,s):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s: str):
        l = len(s)
        # s = list(s)
        if l < 2:
            return s
        max_len = 1
        max_sub = s[0]
        for i in range(l):
            for j in range(i+1,l+1):
                if self.isPalindrome(s[i:j]) and len(s[i:j]) > max_len:
                        max_sub = s[i:j]
                        max_len = len(s[i:j])
        return max_sub


if __name__ == "__main__":
    s = "aaaa"
    #print(s[3:4])
    # result = Solution().isPalindrome(s)
    result = Solution().longestPalindrome(s)
    print(result)
