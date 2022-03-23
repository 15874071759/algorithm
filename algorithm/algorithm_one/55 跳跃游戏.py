#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 3/22/22 8:15 PM 
# @File : 55 跳跃游戏.py 
# @Software: PyCharm

"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
"""


class Solution:
    def canJump(self, nums):
        maxDisdance = 0
        l = len(nums)
        flag = False
        for i in range(l):
            if i <= maxDisdance:
                maxDisdance = max(maxDisdance, i + nums[i])
                if maxDisdance >= l - 1:
                    flag = True
        return flag


if __name__ == "__main__":
    # nums = [3, 2, 1, 0, 4]
    # nums = [2, 3, 1, 1, 4]
    nums = [0, 2, 3]
    s = Solution()
    res = s.canJump(nums)
    print(res)
