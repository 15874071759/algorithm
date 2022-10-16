class Solution:
    def twoSum(self, nums, target):
        hashtable = dict()
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hashtable.keys():
                return [hashtable[temp],i]
            hashtable[nums[i]] = i
        return []




if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    result = s.twoSum(nums, target)
    print(result)
