"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]
"""

class Solution:
    def plusOne(self,digits):
        l = len(digits)-1
        i = l
        digits[l] += 1
        temp = 0
        while  i >= 0:
            if digits[i]+temp <10:
                digits[i] +=temp
                return digits
            else:
                digits[i] = 0
                temp = 1
                if i == 0:
                    digits.insert(0,1)
                i -= 1
        return digits

if __name__ == '__main__':
    digits = [8, 8, 8]
    s = Solution()
    re = s.plusOne(digits)
    print("re",re)