#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 1/24/22 9:57 PM 
# @Author : huff 
# @File : 5.最长回文子串.py 
# @Software: PyCharm

"""给你一个字符串 s，找到 s 中最长的回文子串。"""

class Solution:
    def longestPalindrome(self,s):
        if len(s)<2:
            return s
        maxlen = 1
        begin = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if(j-i+1)> maxlen and self.validPalindromic(s[i:j+1]):
                    maxlen = j-i+1
                    begin = i
        return s[begin:begin+maxlen]

    def validPalindromic(self,s):
        i = 0
        j = len(s)-1
        while i<len(s):
           if s[i] != s[j]:
               return False
           i += 1
           j -=1
        return True


if __name__ == '__main__':
    s = Solution()
    s1 = "babad"
    print(s.longestPalindrome(s1))
    #print(s.validPalindromic(s1))
