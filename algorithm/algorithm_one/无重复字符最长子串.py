#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-05-18 21:19 
# @Author : huff 
# @File : 最长无重复子数组.py 
# @Software: PyCharm

#
# class Solution:
#     def maxLength(self , arr ):
#         if len(arr) < 1:
#             return 0
#         maxLen = 1
#         for i in range(len(arr)-1):
#             maxSub = arr[i]
#             for j in range(i+1,len(arr)):
#                 if maxSub.count(arr[j]) == 0:
#                     maxSub += arr[j]
#                     #print(maxSub)
#                 else:
#                     break
#                 if maxLen < len(maxSub):
#                     maxLen = len(maxSub)
#         return maxLen

# class Solution:
#     def maxLength(self , arr ):
#         arr = list(arr)
#         l = len(arr)
#         if l < 2:
#             return len
#         maxLen = 1
#         maxSub = []
#         for i in range(l):
#             if maxSub.count(arr[i]) > 0:
#                 index = maxSub.index(arr[i])
#                 maxSub = maxSub[index+1:]
#             maxSub.append(arr[i])
#             if maxLen < len(maxSub):
#                 maxLen = len(maxSub)
#         return maxLen

class Solution:
    def lengthOfLongestSubstring(self, arr: str) -> int:
        l = len(arr)
        if l < 2:
            return l
        arr = list(arr)
        maxLen = 1
        maxSub = []
        for i in range(l):
            if maxSub.count(arr[i]) > 0:
                index = maxSub.index(arr[i])
                maxSub = maxSub[index+1:]
            maxSub.append(arr[i])
            if maxLen < len(maxSub):
                maxLen = len(maxSub)
        return maxLen

if __name__ == '__main__':
    s = "dvdf"
    temp = Solution().lengthOfLongestSubstring(s)
    print(temp)
