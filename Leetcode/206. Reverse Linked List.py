from helpers.linked_list import Node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


head = Node(0)
a = Node(1, head)
b = Node(2, a)
c = Node(3, b)
d = Node(4, c)

print(head)

sol = Solution()
new_head = sol.reverseList(head)
print(new_head)