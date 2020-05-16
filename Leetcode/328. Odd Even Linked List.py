# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.nodes = []

    def swapTailWithNext(self, current: ListNode, oddNext: ListNode, oddTail: ListNode):
        next_of_current = current.next
        current.next = oddNext
        if next_of_current:
            next_of_current.next = oddTail.next
        oddTail.next = next_of_current

    def sortOddEven(self, head: ListNode):
        if head.next and head.next.next:
            self.sortOddEven(head.next.next)
        else:
            self.nodes = [head, head]
            return

        self.swapTailWithNext(head, self.nodes[0], self.nodes[1])
        self.nodes[0] = head
        return

    def oddEvenList(self, head: ListNode):
        if not head:
            return head
        self.sortOddEven(head)

        return self.nodes[0]


class Solution2:
    def oddEvenList(self, head: ListNode) -> ListNode:
        temp_odd = ListNode(0)
        temp_even = ListNode(0)
        oddHead = temp_odd
        evenHead = temp_even

        isOdd = True
        while head:
            if isOdd:
                temp_odd.next = head
                temp_odd = head
            else:
                temp_even.next = head
                temp_even = head

            isOdd = not isOdd
            head = head.next

        temp_even.next = None
        temp_odd.next = evenHead.next
        return oddHead.next


temp = None
for i in range(6, 0, -1):
    node = ListNode(i, temp)
    temp = node

Head = temp
# while temp:
#     print(temp.val)
#     temp = temp.next

sol = Solution2()
odd_even = sol.oddEvenList(Head)
while odd_even:
    print(odd_even.val)
    odd_even = odd_even.next
