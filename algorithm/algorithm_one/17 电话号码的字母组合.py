"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]


提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字
"""


class Solution:
    # 队列解法
    def letterCombinations(self, digits: str):
        if not digits: return []

        temp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        digits = list(digits)
        queue = ['']  # 初始化队列
        for k in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                letters = list(temp[k])
                for letter in letters:
                    queue.append(tmp + letter)
        return queue

    # 回溯递归
    def letterCombinations1(self, digits: str):
        if not digits: return []

        temp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        digits = list(digits)
        res = []

        def backtrack(combination, nextdigit):
            if len(nextdigit) == 0:
                res.append(combination)
            else:
                for letter in temp[nextdigit[0]]:
                    backtrack(combination + letter, nextdigit[1:])

        backtrack('', digits)
        return res


if __name__ == '__main__':
    s = Solution()
    digits = '23'
    re = s.letterCombinations1(digits)
    print(re)
