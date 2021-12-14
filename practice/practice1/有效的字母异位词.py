#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-28 21:24 
# @Author : huff 
# @File : 有效的字母异位词.py 
# @Software: PyCharm
"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
 
提示:
1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict.fromkeys(list(s))
        for item1 in dict1.keys():
            dict1[item1]=list(s).count(item1)
        print(dict1)

        dict2 = dict.fromkeys(list(t))
        for item2 in dict2.keys():
            dict2[item2]=list(t).count(item2)
        print(dict2)
        return dict1 == dict2


if __name__ == '__main__':
    x = "aa"
    y = "a"
    s = Solution()
    target = s.isAnagram(x,y)
    print(target)

