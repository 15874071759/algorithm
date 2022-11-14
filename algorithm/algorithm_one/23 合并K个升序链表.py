"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    #1。暴力求解： 遍历所有链表放入数组，数组排序，建立链表
    #2。逐一求解
    def mergeKLists(self, lists):
        result = ListNode(-1)

if __name__ == "__main__":
    s = Solution()

    # 创建链表
    list1 = ListNode(1)
    list2 = ListNode(1)

    cur1 = list1
    cur2 = list2

    cur1.next = ListNode(2)
    cur1 = cur1.next
    cur1.next = ListNode(4)
    cur1 = cur1.next

    cur2.next = ListNode(3)
    cur2 = cur2.next
    cur2.next = ListNode(4)
    cur2 = cur2.next

    # 创建链表数组
    lists = [list1, list2]

    # 遍历链表数组
    # n = len(lists)
    # i = 0
    # while i < n:
    #     while lists[i]:
    #         print(lists[i].val)
    #         lists[i] = lists[i].next
    #     i +=1

    # 调合并K个数组函数
    res = s.mergeKLists(lists)
    while res:
        print(res.val)
        re = res.next
