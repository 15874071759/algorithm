"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
子数组是数组中元素的连续非空序列。

示例 1：
输入：nums = [1,1,1], k = 2
输出：2

示例 2：
输入：nums = [1,2,3], k = 3
输出：2


提示：
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""


class Solution:
    def subarraySum(self, nums, k):
        '''超时解法'''
        count = 0
        i = 0
        while i < len(nums):
            sum = 0
            j = i
            while 0 <= j <= i:
                sum += nums[j]
                if sum == k:
                    count += 1
                j -= 1
            i += 1
        return count

        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,-1,-1):
        #         sum += nums[j]
        #         if sum == k :
        #              count +=1
        # return count






if __name__ == '__main__':
    so = Solution()
    # nums = [1, 2, 3]
    # k = 3
    nums = [1, 1, 1]
    k = 2
    # nums =[1, 2, 1, 2, 1]
    # k = 3
    # nums =[-1, -1, 1]
    # k = 0
    # nums = [1, -1, 0]
    # k = 0
    # nums = [28, 54, 7, -70, 22, 65, -6]
    # k = 100
    # nums = [-313,-462,381,-374,-249,-123,704,477,982,-684,-372,779,-68,593,-254,-930,-142,-369,811,-621,682,167,-125,565,438,-137,-683,257,-454,-256,306,635,-571,52,-59,-411,628,895,-509,-9,-722,926,79,392,-720,94,-190,902,96,486,-147,363,-24,604,-265,-680,529,-462,-477,-384,991,319,-520,-799,-95,705,528,684]
    # k = 339
    re = so.subarraySum(nums,k)
    print(re)
