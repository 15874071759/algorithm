#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-05 10:48 
# @Author : huff 
# @File : 三数之和.py 
# @Software: PyCharm

'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

提示：
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


class Solution:
    # 1.暴力解法，超时限制
    def threeSum1(self, nums):
        #nums.sort()
        l = len(nums)
        res = []
        for i in range(l):
            for j in range(i,l):
                for k in range(j,l):
                    if i != j and j != k and i != k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            temp = sorted([nums[i], nums[j], nums[k]])
                            # print(temp)
                            if temp not in res:
                                res.append(temp)
        return res

    #双指针
    def threeSum(self,nums):

        nums.sort()
        l = len(nums)
        res = []
        for i in range(l):
            #跳过重复值
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            right = l-1
            for left in range(i+1,l):
                # 跳过重复值
                if left > i+1 and nums[left] == nums[left - 1]:
                    continue
                while left < right and nums[left] + nums[right] > target:
                    right -=1

                if left == right:
                    break
                if nums[left] + nums[right] == target:
                    res.append([nums[i],nums[left],nums[right]])

        return res




if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    re = s.threeSum(nums)
    print(re)