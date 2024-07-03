"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

示例 1:
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:
输入: nums = [2,3,0,1,4]
输出: 2

提示:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
题目保证可以到达 nums[n-1]
"""

class Solution:
    def jump(self,nums):
        cur_distance = 0 # 当前局部可以走的最远下标
        next_distance = 0 # 下一步局部可以走的最远下标
        step = 0

        for i in range(len(nums)-1):
            next_distance = max(nums[i]+i,next_distance)
            if i == cur_distance: #到当前最大距离下标
                step +=1 #需要走下一步
                cur_distance = next_distance # 更新当前可以走的最远距离下标
                # if next_distance >= len(nums)-1:
                #     break
        return step


if __name__ == '__main__':

    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    nums = [1, 2, 3]
    re = solution.jump(nums)
    print(re)