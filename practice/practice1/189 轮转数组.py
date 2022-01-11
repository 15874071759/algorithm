#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 1/11/22 12:28 PM 
# @Author : huff 
# @File : 189 轮转数组.py 
# @Software: PyCharm
'''
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
 

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
'''

class Solution:
    def rotate(self, nums: list, k: int) -> None:
        '''1.第一种'''
        # l = len(nums)
        # k = k%l
        # nums1 = nums[0:l - k]
        # nums2 = nums[l - k:l]
        # nums2.extend(nums1)
        # for i in range(l):
        #     nums[i]=nums2[i]
        '''2.第二种'''
        l = len(nums)
        k = k%l
        temp = []
        for i in range(l):
            temp.append(nums[(i+l-k)%l])
            #print(temp)
        for i in range(l):
            nums[i]=temp[i]
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    s = Solution()
    s.rotate(nums,k)
    print('排序好的数组：',nums)