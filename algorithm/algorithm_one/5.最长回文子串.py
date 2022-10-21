#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 1/24/22 9:57 PM 
# @Author : huff 
# @File : 5.最长回文子串.py 
# @Software: PyCharm

"""给你一个字符串 s，找到 s 中最长的回文子串。"""
#暴力解法
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

#动态规划
class Solution1:
    def longestPalindrome1(self,s):
        n = len(s)
        if n < 2:
            return s
        maxLen = 1
        begin = 0
        #dp[i][j]表示s[s:j+1]是否是回文子串
        dp =[[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True

        #枚举子串长度
        for l in range(2,n+1):
            for i in range(n):
                #右边界
                j = i+l-1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j]=False
                else:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1 > maxLen:
                    maxLen = j-i +1
                    begin = i
        return s[begin:begin+maxLen]


if __name__ == '__main__':
    s = Solution1()
    s1 = "babada"
    print(s.longestPalindrome1(s1))
    s = Solution()
    s1 = "babada"
    print(s.longestPalindrome(s1))
    #print(s.validPalindromic(s1))

