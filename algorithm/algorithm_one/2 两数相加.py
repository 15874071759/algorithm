#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2/22/22 4:45 PM 
# @Author : huff 
# @File : 2 两数相加.py 
# @Software: PyCharm

"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        head = l3
        step = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            # print(x)
            # print(y)
            reslut = x + y + step
            step = reslut // 10
            #print(reslut % 10)
            head.next = ListNode(reslut % 10)
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if step == 1:
            head.next = ListNode(1)
        return l3.next


if __name__ == "__main__":
    # l1 = [2,4,3]
    # l2 = [5,6,4]
    list1 = ListNode(2)
    list2 = ListNode(3)
    list2.next = ListNode(4)
    while list2 or list1:
        print(list2.val if list2 else 0)
        print(list1.val if list1 else 0)
        list2 = list2.next if list2 else None
        list1 = list1.next if list1 else None
    # list1.next = list11 = ListNode(4)
    # list11.next = list12 = ListNode(3)
    # list2 = ListNode(5)
    # list2.next = list21 = ListNode(6)
    # list21.next = list22 = ListNode(4)
    # temp = Solution()
    # re = temp.addTwoNumbers(list1, list2)
    # while re:
    #     print(re.val)
    #     re = re.next

