from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertNewNode(self, head: TreeNode, newNode: TreeNode):
        if newNode.val < head.val:
            if head.left:
                self.insertNewNode(head.left, newNode)
            else:
                head.left = newNode

        else:
            if head.right:
                self.insertNewNode(head.right, newNode)
            else:
                head.right = newNode

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        head = TreeNode(preorder[0])
        for val in preorder[1:]:
            self.insertNewNode(head, TreeNode(val))

        return head