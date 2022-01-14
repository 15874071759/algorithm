#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-28 11:29 
# @Author : huff 
# @File : 多数元素.py 
# @Software: PyCharm

'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2

进阶：
尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
'''
class Solution:
    def majorityElement(self, nums: list) -> int:
        dict1 = dict.fromkeys(nums)
        for item in dict1.keys():
            dict1[item] = nums.count(item)
            if dict1[item]>len(nums)/2:
                return item


if __name__ == '__main__':
    list1 = [2,2,1,1,1,1,2]
    s = Solution()
    target = s.majorityElement(list1)
    print(target)
