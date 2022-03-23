#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 3/22/22 4:44 PM 
# @File : 53 最大子数组和.py 
# @Software: PyCharm

"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23
"""


class Solution:
    def maxSubArray(self, nums):
        maxSum = nums[0]
        temp = 0
        l = len(nums)
        for i in range(l):
            temp = max(nums[i],temp+nums[i])
            maxSum = max(maxSum,temp)
        return maxSum


if __name__ == "__main__":
    nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
   # print(sum(nums))
    s = Solution()
    res = s.maxSubArray(nums)
    print(res)
