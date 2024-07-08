"""
给定两个字符串 s 和 t ，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例 1：
输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。

示例 2：
输入：s = "", t = "y"
输出："y"

提示：
0 <= s.length <= 1000
t.length == s.length + 1
s 和 t 只包含小写字母
"""

class Solution:
    def findTheDifference(self, s, t):
        count = {}
        for item_t in t:
            if item_t in count.keys():
                count[item_t] +=1
            else:
                count[item_t] = 1
        for k in s:
            if k in count.keys():
                count[k] -= 1
        re = ''
        for k in count.keys():
            if count[k] > 0:
                re +=k
        return re

if __name__ == '__main__':
    solution = Solution()
    s = "abcd"
    t = "abcde"
    s = ""
    t = "y"
    re = solution.findTheDifference(s,t)
    print(re)