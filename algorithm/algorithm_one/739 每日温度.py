#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 3/16/22 3:49 PM 
# @File : 739 每日温度.py 
# @Software: PyCharm

"""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
其中 answer[i] 是指在第 i 天之后，才会有更高的温度。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
"""


class Solution:
    """暴力解法"""

    def dailyTemperatures1(self, temperatures):
        l = len(temperatures)
        result = [0 for x in range(l)]
        # print(result)
        for i in range(l):
            j = i + 1
            flag = False
            while j < l:
                if temperatures[i] < temperatures[j]:
                    result[i] = j - i
                    # flag = True
                    break
                j += 1
            # if not flag:
            # result.append(0)
        return result

    def dailyTemperatures(self, temperatures):
        l = len(temperatures)
        result = [0] * l
        stack = []
        # print(stack)
        for i in range(l):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result


if __name__ == "__main__":
    temperatures = [30, 20, 50, 10, 30]
    s = Solution()
    res = s.dailyTemperatures(temperatures)
    print(res)
