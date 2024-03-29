"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。


示例 1：

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:

输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：

输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
"""


class Solution:
    # 逻辑有问题
    def isMatch1(self, s: str, p: str) -> bool:
        if len(s) > len(p):
            p = " " * (len(s) - len(p)) + p
        for k in range(len(s)):
            i = len(p) - 1 - k
            if p[i] != '.' and p[i] != '*':
                if p[i] != s[i]:
                    return False
            # if p[j] == '.':
            #     break
            if p[i] == '*':
                if p[i - 1] != s[i] and p[i - 1] != '.':
                    return False
                if p[i - 2] != s[i] and p[i - 1] != '.':
                    return False
                if p[i -1] != s[i-1] and p[i - 1] != '.':
                    return False
        return True

    def isMatch(self, s: str, p: str) -> bool:

        def matches(i,j):
            if i ==0:
                return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]

        m,n=len(s),len(p)
        f=[[False]*(n+1) for _ in range(m+1)]
        f[0][0]=True
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1]=='*':
                    f[i][j] |= f[i][j-2]
                    if matches(i,j-1):
                     f[i][j] |=f[i-1][j]
                else:
                    if matches(i,j):
                        f[i][j] |= f[i-1][j-1]
        return f[m][n]




if __name__ == "__main__":
    s = "aab"
    p = "c*a*b"
    # s = "aaa"
    # p = "a*"
    ss = Solution()
    res = ss.isMatch(s, p)
    print(res)
