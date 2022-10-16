"""
给你一个整数数组 nums，请你将该数组升序排列。
示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
"""

class solution:
    def sort(self,nums):
        l = len(nums)
        for i in range(l-1):
            min = i
            for j in range(i+1,l):
                if nums[j]<nums[min]:
                    min = j
                    #print("内层：",min)
            #print("外层：",min)
            nums[min],nums[i] = nums[i],nums[min]
        return nums


if __name__ == "__main__":
    nums = [5, 2, 3, 1]
    s = solution()
    res = s.sort(nums)
    print("选择排序后的数组：",res)

