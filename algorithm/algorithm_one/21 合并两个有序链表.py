"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 迭代
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        # 合并后的链表
        res = ListNode(0)
        result = res
        l1 = ListNode(0, list1).next
        l2 = ListNode(0, list2).next
        val1 = 0
        val2 = 0
        while l1 != None or l2 != None:

            if l1 != None:
                val1 = l1.val
            if l2 != None:
                val2 = l2.val
            # print("val1:", val1)
            # print("val2:", val2)

            # print("res.val:",res.val)

            if val1 <= val2:
                res.next = ListNode(val1)
                if l1 != None:
                    l1 = l1.next
                else:
                    break
            else:
                res.next = ListNode(val2)
                # if l1.next != None:
                if l2 != None:
                    l2 = l2.next
                else:
                    break
            res = res.next

        res.next = l1 if l1 is not None else l2
        return result.next

    #参考写法
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next



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

    # 遍历链表
    # while list1 :
    #     print(list1.val)
    #     list1 = list1.next
    # while list2:
    #     print(list2.val)
    #     list2 = list2.next

    re = s.mergeTwoLists1(list1, list2)
    while re:
        print(re.val)
        re = re.next
