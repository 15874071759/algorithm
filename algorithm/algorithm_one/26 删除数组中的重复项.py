
class Solution:
    # set去重，有开辟新的空间
    def removeDuplicates1(self, nums):
        # print(nums)
        re = list(set(nums))
        # print(re)
        return len(re)
    # 双指针，不开劈新的空间
    def removeDuplicates(self, nums):
        l = len(nums)
        slow = 1
        fast = 1
        for fast in range(1,l):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow +=1

        #print(nums)

        return slow

if __name__ == "__main__":
    num = [0,1,1,1,2,3,5,5]
    s = Solution()
    re = s.removeDuplicates(num)
    print(re)