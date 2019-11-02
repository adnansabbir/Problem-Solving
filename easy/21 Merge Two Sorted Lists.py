class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = sorted_list = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                sorted_list.next = l1
                l1 = l1.next
            else:
                sorted_list.next = l2
                l2 = l2.next

            sorted_list = sorted_list.next

        sorted_list.next = l1 or l2

        return head.next

# TimeComplexity -> O(n) where n = max length between l1 and l2
