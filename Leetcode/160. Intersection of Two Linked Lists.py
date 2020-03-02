# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        headALen = 0
        headBLen = 0

        headATemp = headA
        headBTemp = headB

        while headATemp and headATemp.next:
            headALen += 1
            headATemp = headATemp.next

        while headBTemp and headBTemp.next:
            headBLen += 1
            headBTemp = headBTemp.next

        diff = abs(headALen - headBLen)

        if headALen > headBLen:
            while diff:
                headA = headA.next
                diff -= 1
        else:
            while diff:
                headB = headB.next
                diff -= 1

        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None
