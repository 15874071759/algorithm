"""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

示例 1:
输入: nums = [1,2,3,4]
输出: [24,12,8,6]

示例 2:
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]

提示：
2 <= nums.length <= 105
-30 <= nums[i] <= 30
保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
"""

class Solution:
    def productExceptSelf(self, nums):

        L = [1 for i in nums]
        R = [1 for j in nums]

        for x in range(1,len(nums)):
            L[x] = L[x-1] * nums[x-1]

        for y in range(len(nums)-2,-1,-1):
            R[y] = R[y+1] * nums[y+1]

        rev = []
        # print(L,R)

        for z in range(len(nums)):
            rev.append(L[z]*R[z])

        return rev





if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    nums = [-1,1,0,-3,3]
    re = solution.productExceptSelf(nums)
    print(re)