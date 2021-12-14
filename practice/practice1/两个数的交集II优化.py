#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-02 19:56 
# @Author : huff 
# @File : 两个数的交集II优化.py 
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


class Solution:
    def intersect(self, nums1, nums2):
        if len(nums2)>len(nums1): #保证
            nums2,nums1 = nums1,nums2
        dict1 = dict.fromkeys(nums1)
        for item in nums1:
            dict1[item]=nums1.count(item)
        print('哈希集合:',dict1)
        result = []
        for i in nums2:
            if i in dict1.keys() and dict1[i]>0:
                result.append(i)
                dict1[i]-=1
        return result


if __name__ == '__main__':
    nums1 = [4, 4, 9, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    s = Solution()
    result = s.intersect(nums1,nums2)
    print(result)