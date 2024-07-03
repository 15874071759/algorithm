'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2


提示：
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

'''


class Solution:
    def majorityElement(self,nums):
        key = len(nums)/2
        # print('key',key)
        map = {}
        for i in range(len(nums)):
            if nums[i] in map.keys():
                map[nums[i]] +=1
            else:
                map[nums[i]] = 1
        # print('map',map)
        for j in map.keys():
            if map[j] > key:
                return j

        # nums.sort()
        # print(nums)
        # return nums[len(nums) // 2]



if __name__ == '__main__':

    nums = [3, 2, 3]
    # nums = [2, 2, 1, 1, 1, 2, 2]
    solution = Solution()
    re = solution.majorityElement(nums)
    print(re)