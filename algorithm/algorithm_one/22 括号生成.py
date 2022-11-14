"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

提示：

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int):

        res = []
        cur_str = ''
        def dfs(cur_str,left,right,n):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left:左括号已经使用的个数
            :param right:左括号已经使用的个数
            :param n:
            :return:
            """
            if left == n and right ==n:
                res.append(cur_str)
                return
            if left < right:
                return
            if left < n:
                dfs(cur_str+"(",left+1,right,n)
            if right < n:
                dfs(cur_str+")",left,right+1,n)
        dfs(cur_str,0,0,n)
        return res





if __name__ == '__main__':
    s = Solution()
    n = 3
    res = s.generateParenthesis(n)
    print(res)