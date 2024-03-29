#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-20 11:54 
# @Author : huff 
# @File : 287 寻找重复数.py 
# @Software: PyCharm

'''
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。
你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3

示例 3：
输入：nums = [1,1]
输出：1

示例 4：
输入：nums = [1,1,2]
输出：1
 
提示：
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
 
进阶：
如何证明 nums 中至少存在一个重复的数字?
你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
'''
class Solution:
    def findDuplicate(self, nums: list) -> int:
        left,right = 1,len(nums)-1
        while left < right:
            mid = left + (right - left)//2
            count = 0
            for num in nums:
               if num <= mid:
                   count +=1
            if count <= mid:
                left = mid +1
            else:
                right = mid
        return left


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 3]
    s = Solution()
    result = s.findDuplicate(nums)
    print('重复数是：',result)