"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:

 输入："aabcccccaaa"
 输出："a2b1c5a3"
示例2:

 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
提示：

字符串长度在[0, 50000]范围内。
"""

class Solution:
    def compressString(self, S: str) -> str:

        if len(S) == 0:
            target_str = ''
        target_str = S[0]
        temp_count = 0
        for i in range(len(S)):
            if target_str[-1] != S[i]:
                target_str += str(temp_count)
                target_str += S[i]
                temp_count = 1
            else:
                temp_count += 1
            if i == len(S)-1:
                target_str += str(temp_count)

        if len(target_str) >= len(S):
            target_str = S

        return target_str


if __name__ == '__main__':
    s = Solution()
    test = 'aabcccccaaa'
    re = s.compressString(test)
    print(re)
