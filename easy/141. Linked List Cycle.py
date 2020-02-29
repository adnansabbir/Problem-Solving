class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        if head.next and head.next.next:
            slow = head.next
            fast = slow.next

            while fast.next and fast.next.next:
                if slow == fast:
                    return True

                slow = slow.next
                fast = fast.next.next

        else:
            if head.next and head.next == head:
                return True

        return False
