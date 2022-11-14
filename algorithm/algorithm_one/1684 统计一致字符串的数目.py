"""
给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。

请你返回 words 数组中 一致字符串 的数目。

示例 1：

输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
输出：2
解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。
示例 2：

输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
输出：7
解释：所有字符串都是一致的。
示例 3：

输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
输出：4
解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words):

        words_len = len(words)
        count = 0

        def isConsistentString(word):
            Flag = True
            for k in range(len(word)):
                if word[k] not in allowed:
                    Flag = False
                    break
            return Flag
        for i in range(words_len):
            if isConsistentString(words[i]):
                count +=1
        return count



if __name__ == '__main__':
    # allowed = "ab"
    # words = ["ad", "bd", "aaab", "baa", "badab"]
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    s = Solution()
    re = s.countConsistentStrings(allowed,words)
    print(re)