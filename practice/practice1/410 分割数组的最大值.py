#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-31 10:36 
# @Author : huff 
# @File : 410 分割数组的最大值.py 
# @Software: PyCharm

'''
给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。
设计一个算法使得这 m 个子数组各自和的最大值最小。

示例 1：
输入：nums = [7,2,5,10,8], m = 2
输出：18
解释：
一共有四种方法将 nums 分割为 2 个子数组。 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

示例 2：
输入：nums = [1,2,3,4,5], m = 2
输出：9

示例 3：
输入：nums = [1,4,4], m = 3
输出：4
 
提示：
1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
'''

class Solution:
    def splitArray(self, nums: list, m: int) -> int:
        def sumSplit(maxValue):
            sum , split = 0 ,1
            for num in nums:
                if sum + num > maxValue:
                    sum = 0
                    split +=1
                #else:
                sum +=num
            return split

        left,right = max(nums),sum(nums)
        while left < right:
            mid = left + (right - left)//2
            if sumSplit(mid)>m:
                left = mid +1
            else:
                right = mid
        return left


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    s = Solution()
    result = s.splitArray(nums,m)
    print('最大值最小：',result)
