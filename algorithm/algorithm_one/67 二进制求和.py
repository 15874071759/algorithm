"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

示例 1：
输入:a = "11", b = "1"
输出："100"

示例 2：
输入：a = "1010", b = "1011"
输出："10101"

提示：
1 <= a.length, b.length <= 104
a 和 b 仅由字符 '0' 或 '1' 组成
字符串如果不是 "0" ，就不含前导零
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp_a = a if len(a)>len(b) else b #较长
        temp_a = temp_a[::-1]
        temp_b = b if len(b)<len(a) else a #较短
        temp_b = ''.join(reversed(temp_b))
        temp_c = []
        temp = 0
        print(temp_a,temp_b)

        for i in range(len(temp_b)):
            temp_c.append(str((temp + int(temp_a[i]) + int(temp_b[i]))%2))
            temp = (temp + int(temp_a[i]) + int(temp_b[i]))//2
        for j in range(len(temp_b),len(temp_a)):
            temp_c.append(str((temp + int(temp_a[j])) % 2))
            temp = (temp + int(temp_a[j]))//2
        print(temp)
        if temp>0:
            temp_c.append(str(temp))
        print(temp_c)
        return  ''.join(reversed(temp_c))

        # 直接进制转换也可以实现
        # return '{0:b}'.format(int(a,2)+int(b,2)) # int(a,2)表示二进制转十进制








if __name__ == '__main__':
    a = "11"
    b = "1"
    # a = "1010"
    # b = "1011"
    # a = "1"
    # b = "111"
    a ="100"
    b ="110010"
    s = Solution()
    re = s.addBinary(a, b)
    print(re)
