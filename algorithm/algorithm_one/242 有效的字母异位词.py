"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

提示:
1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母

进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
class Solution:
    def isAnagram(self, s, t):
        count_s = {}
        count_t = {}
        # for item_s in s:
        #     if item_s in count_s.keys():
        #         count_s[item_s] +=1
        #     else:
        #         count_s[item_s] = 1
        count_s = {i:s.count(i) for i in s}

        # for item_t in t:
        #     if item_t in count_t.keys():
        #         count_t[item_t] +=1
        #     else:
        #         count_t[item_t] = 1
        count_t = {i:t.count(i) for i in t}
        # print(count_s,count_t)

        if set(count_s.keys()) - set(count_t.keys()) or set(count_t.keys()) - set(count_s.keys()):
            return False
        for item in count_t.keys():
            if count_t[item] !=count_s[item]:
                return False
        return True




if __name__ == '__main__':
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    # s = "rat"
    # t = "car"
    re = solution.isAnagram(s,t)
    print(re)
    # c = lambda a:a*3
    # print(c(4))