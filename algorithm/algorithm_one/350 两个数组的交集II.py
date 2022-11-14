"""
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，
应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
"""

import collections
class Solution:
    #排序+双指针
    def intersection1(self,nums1,nums2):
        nums1.sort()
        nums2.sort()
        l1 = 0
        l2 = 0
        temp = []
        while l1<len(nums1) and l2<len(nums2):
            if nums1[l1] < nums2[l2]:
                l1 +=1
            elif nums1[l1] > nums2[l2]:
                l2 +=1
            else:
                temp.append(nums1[l1])
                l1 +=1
                l2 +=1
        return temp

    #哈希表
    def intersection(self, nums1, nums2):
        if len(nums1)>len(nums2):
            return self.intersection(nums2,nums1)
        # collections.Counter() 集合计数器
        m = collections.Counter(nums1)
        temp = []
        for i in range(len(nums2)):
            if nums2[i] in m and m[nums2[i]] > 0:
                temp.append(nums2[i])
                m[nums2[i]] -=1
        return temp






if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    s = Solution()
    res = s.intersection(nums1,nums2)
    print("res:",res)