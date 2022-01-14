#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-27 23:36 
# @Author : huff 
# @File : 合并两个有序数组.py 
# @Software: PyCharm

'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
 提示：

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109

'''

class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #nums1 = nums1[0:m] #使用切片相当于重新生成了一个list对象，题目本意在于nums1是原来对象，不生成新的对象
        del nums1[m:m+n]
        nums1.extend(nums2) #作用于原对象
        #print(nums1)
        #return sorted(nums1) #sorted(nums1)会生成一个新的对象
        return nums1.sort() #sort在原对象上排序

list

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s = Solution()
    s.merge(nums1,m,nums2,n)
    #print(id(nums1))
    print(nums1)