#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-06 11:14 
# @Author : huff 
# @File : 283 移动零.py 
# @Software: PyCharm

'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''

class Solution:
    def moveZeroes(self, nums: list) -> None:

        # for i in range(len(nums)-1):
        #     for j in range(len(nums)-1):
        #         if nums[j] == 0:
        #              nums[j],nums[j+1]=nums[j+1],nums[j]
        left = right =0
        while right < len(nums):
            if nums[right] !=0:
                nums[right],nums[left]=nums[left],nums[right]
                left +=1
            right +=1





if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(nums)
    print('排序好的数组：',nums)