#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-30 22:47 
# @Author : huff 
# @File : 两个数的交集II.py 
# @Software: PyCharm

'''
给定两个数组，编写一个函数来计算它们的交集。
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 
说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''

#待优化
import copy
class Solution:
    def intersect(self, nums1, nums2):
        dict1 = dict.fromkeys(nums1)
        dict2 = dict.fromkeys(nums2)
        for item in dict1:
            dict1[item] = nums1.count(item)
        for item in dict2:
            dict2[item] = nums2.count(item)
        #print(dict1)
        #print(dict2)
        #找出不重复的值交集
        result = list(dict2.keys()&dict1.keys())
        #print(result)
        s = []
        target = copy.deepcopy(result)
        #找出重复的值，并用重复的值加到结果list中
        for i in result:
             temp = min(dict1[i],dict2[i])
             #print(temp)
             if temp > 1:
                 s = [i]*(temp-1)
                 #print('数组',s)
                 target.extend(s)

        return target



if __name__ == '__main__':

    nums1 = [4,4, 9,9, 5]
    nums2 = [9, 4, 9, 8, 4]
    s = Solution()
    result = s.intersect(nums1,nums2)
    print(result)
