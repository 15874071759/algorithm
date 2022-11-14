#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-16 22:58 
# @Author : huff 
# @File : 88 合并两个有序数组.py 
# @Software: PyCharm

"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，
其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。

示例 3：
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
 
提示：
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 
进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？
"""


class Solution:
    def merge1(self, nums1, m, nums2, n):
        # 1.直接合并后排序
        # nums1[m:]=nums2
        # nums1.sort()
        # 2.双指针
        # nums3 = []
        # pointer1,pointer2 = 0,0
        # while pointer1 < m or pointer2 < n:
        #     if pointer1 == m:
        #         nums3.append(nums2[pointer2])
        #         pointer2 +=1
        #     elif pointer2 == n:
        #         nums3.append(nums1[pointer1])
        #         pointer1 +=1
        #     elif nums1[pointer1]<nums2[pointer2]:
        #         nums3.append(nums1[pointer1])
        #         pointer1 +=1
        #     else:
        #         nums3.append(nums2[pointer2])
        #         pointer2 +=1
        # nums1[:] = nums3

        p1 = m - 1
        p2 = n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1

    # 直接合并排序
    def merge2(self, nums1, m: int, nums2, n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()

    # 逆向双指针
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        re = m + n - 1
        l1 = m - 1
        l2 = n - 1
        while l1 >= 0 or l2 >= 0:
            if l1 == -1:
                nums1[re] = nums2[l2]
                l2 -= 1
            elif l2 == -1:
                nums1[re] = nums1[l1]
                l1 -= 1
            elif nums1[l1] > nums2[l2]:
                nums1[re] = nums1[l1]
                l1 -= 1
            else:
                nums1[re] = nums2[l2]
                l2 -= 1
            re -= 1

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print('排序好的数组：', nums1)
