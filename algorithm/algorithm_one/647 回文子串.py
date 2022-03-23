#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 3/16/22 5:12 PM 
# @File : 647 回文子串.py 
# @Software: PyCharm

"""
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
回文字符串 是正着读和倒过来读一样的字符串。
子字符串 是字符串中的由连续字符组成的一个序列。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""


class Solution:
    def countSubstrings(self, s):
        l = len(s)
        table = [[False for i in range(l)] for j in range(l)]
        for i in range(l):
            table[i][i] = True
        # print(table)
        # 子串长度
        for length in range(2, l + 1):
            # 起始下标
            for i in range(l):
                j = i + length - 1
                if j >= l:
                    break
                if s[i] == s[j]:
                    if j - i >= 3:
                        table[i][j] = table[i + 1][j - 1]
                    else:
                        table[i][j] = True
        #print(table)
        # for i in range(l):
        #     for j in range(l):
        #         if table[i][j] == True and i != j:
        #             print("i,j",i,j)
        temp = [t for item in table for t in item]
        return temp.count(True)


if __name__ == "__main__":
    ss = "xkjkqlajprjwefilxgpdpebieswu"
    #print(len(ss))
    s = Solution()
    res = s.countSubstrings(ss)
    print(res)
    #print(0.2+0.1)
