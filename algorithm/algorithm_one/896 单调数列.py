"""
如果数组是单调递增或单调递减的，那么它是 单调 的。
如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i]> = nums[j]，那么数组 nums 是单调递减的。
当给定的数组 nums 是单调数组时返回 true，否则返回 false。

示例 1：
输入：nums = [1,2,2,3]
输出：true

示例 2：
输入：nums = [6,5,4,4]
输出：true

示例 3：
输入：nums = [1,3,2]
输出：false

提示：
1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""

class Solution:
    def isMonotonic(self, nums):
        flag = True
        if len(nums) == 1:
            return True


        if nums[len(nums)-1] > nums[0]:
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1] <0:
                    flag = False
        elif nums[len(nums)-1] < nums[0]:
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1] >0:
                    flag = False
        else:
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1] !=0:
                    flag = False
        return flag






if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 2, 3]
    nums = [6, 5, 4, 4]
    nums = [1, 3, 2]
    re = solution.isMonotonic(nums)
    print(re)