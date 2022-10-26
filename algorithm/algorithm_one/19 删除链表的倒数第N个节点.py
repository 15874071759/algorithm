"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#计算链表长度，暴力解法
class Solution:
    def removeNthFromEnd(self, head:ListNode, n):
        tmp = head
        len = 0
        while tmp:
            tmp = tmp.next
            len +=1
        k = len - n
        # print(k)

        temp = ListNode(0,head)
        cur = temp
        for _ in range(k):
            cur = cur.next
        cur.next = cur.next.next
        return temp.next






if __name__ == "__main__":
    s = Solution()
    #head = [1, 2, 3, 4, 5]
    head = ListNode(1)
    curNode = head
    for i in range(2,6):
        curNode.next = ListNode(i)
        curNode = curNode.next

    n = 2
    re = s.removeNthFromEnd(head,n)

    while re!=None:
        print(re.val)
        re = re.next
