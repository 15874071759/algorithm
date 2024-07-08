"""
给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。

示例 1:
输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。

示例 2:
输入: s = "aba"
输出: false

示例 3:
输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)

提示：
1 <= s.length <= 104
s 由小写英文字母组成
"""

class Solution:
    def repeatedSubstringPattern(self, s):
        return (s+s).find(s,1) !=len(s)



if __name__ == '__main__':
    solution = Solution()
    s = "abab"
    re = solution.repeatedSubstringPattern(s)
    print(re)