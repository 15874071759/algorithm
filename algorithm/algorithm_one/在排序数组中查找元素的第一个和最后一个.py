#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-07 19:41 
# @Author : huff 
# @File : 在排序数组中查找元素的第一个和最后一个.py 
# @Software: PyCharm
'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 
示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
 
提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
'''

class Solution:
    def searchRange(self,nums,target):
        l = len(nums)
        if l == 0:
            return [-1,-1]
        left,right = 0,l-1
        result = []

        while left<right:  #二分查找找起始点
            mid = left + (right-left)//2
            print('左区间中位：',mid)
            if nums[mid]< target:
                left = mid+1
            else:
                right = mid
        result.append(left if nums[left]==target else -1)

        left,right = 0,l-1
        while left<right: #二分查找终点
            mid = left +(right-left+1)//2
            print('右区间中位：',mid)
            if nums[mid]<= target:
                left = mid
            else:
                right = mid-1
        result.append(right if nums[right]==target else -1)
        return result






if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    s = Solution()
    result = s.searchRange(nums,target)
    print('数组区间是：',result)