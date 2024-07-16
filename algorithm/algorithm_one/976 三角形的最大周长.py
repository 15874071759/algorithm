"""
给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回 0。

示例 1：
输入：nums = [2,1,2]
输出：5
解释：你可以用三个边长组成一个三角形:1 2 2。

示例 2：
输入：nums = [1,2,1,10]
输出：0
解释：
你不能用边长 1,1,2 来组成三角形。
不能用边长 1,1,10 来构成三角形。
不能用边长 1、2 和 10 来构成三角形。
因为我们不能用任何三条边长来构成一个非零面积的三角形，所以我们返回 0。

提示：
3 <= nums.length <= 104
1 <= nums[i] <= 106
"""

class Solution:
    def largestPerimeter(self, nums) -> int:
        """排序+贪心：不失一般性，我们假设三角形的边长 a,b,c 满足 a≤b≤c，那么这三条边组成面积不为零的三角形的充分必要条件为 a+b>c。
        基于此，我们可以选择枚举三角形的最长边 c，而从贪心的角度考虑，我们一定是选「小于 c 的最大的两个数」作为边长 a 和 b，
        此时最有可能满足 a+b>c，使得三条边能够组成一个三角形，且此时的三角形的周长是最大的
        """
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1]+nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0


if __name__ == '__main__':
    nums = [2,1,2]
    nums = [1, 2, 1, 10]
    s = Solution()
    result = s.largestPerimeter(nums)
    print(result)