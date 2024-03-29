"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5
"""


class solution:
    def reversePairs(self, nums):
        l = len(nums)
        count = 0
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] > nums[j]:
                    count +=1
        return count


if __name__ == "__main__":
    nums = [7, 5, 6, 4]
    s = solution()
    res = s.reversePairs(nums)
    print("res:", res)
