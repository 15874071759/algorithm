#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-05 23:15 
# @Author : huff 
# @File : 盛最多水的容器.py 
# @Software: PyCharm

'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
示例 3：

输入：height = [4,3,2,1,4]
输出：16
示例 4：

输入：height = [1,2,1]
输出：2
'''


class Solution:
    def maxArea(self, height: list) -> int:
        # l = len(height)
        # res = []
        # for i in range(l-1):
        #     for j in range(i+1,l):
        #         temp = (j-i)*min(height[i],height[j])
        #         res.append(temp)
        # result = max(res)
        # return  result
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            if height[left] < height[right]:
                ans = height[left] * (right - left)
                left += 1
            else:
                ans = height[right] * (right - left)
                right -= 1
            area = max(area, ans)
        return area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    result = s.maxArea(height)
    print('最大值:\t', result)
