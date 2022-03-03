#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 3/3/22 3:04 PM 
# @Author : huff 
# @File : 20 有效的括号.py 
# @Software: PyCharm

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 
示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true
"""


class Solution:
    def isValid(self, s):
        temp = list(s)
        # print(temp[-1])
        l = len(temp)
        if l % 2 == 1:
            return False
        keys = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        # print(keys.keys())
        # print(keys.values())
        stack = []
        for ch in temp:
            if ch in keys.keys():
                stack.append(ch)
                # print(stack)
            else:
                if not stack or ch != keys[stack[-1]]:
                    return False
                stack.pop()

        # print(stack)
        return not stack


if __name__ == "__main__":
    temp = "){"
    s = Solution()
    print(s.isValid(temp))
