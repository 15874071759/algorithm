"""
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

示例  1：
输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。

示例  2：
输入：mat = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
输出：8

示例 3：
输入：mat = [[5]]
输出：5

提示：
n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""

class Solution:
    def diagonalSum(self, mat) -> int:
        sum = 0
        for i in range(len(mat)):
            # print(mat[i][i],mat[i][len(mat)-1-i])
            sum += mat[i][i] + mat[i][len(mat)-1-i]
        if len(mat) % 2 == 1:
            sum -= mat[len(mat)//2][len(mat)//2]
        return sum



if __name__ == '__main__':
    solution = Solution()
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    mat = [[5]]
    re = solution.diagonalSum(mat)
    print(re)