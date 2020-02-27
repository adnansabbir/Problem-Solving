# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmetric(self, root: TreeNode, root_copy: TreeNode = None) -> bool:
        if not root_copy:
            root_copy = root

        if not (root or root_copy):
            return True
        elif root and root_copy:
            return root.val == root_copy.val \
                   and self.isSymmetric(root.left, root_copy.right) \
                   and self.isSymmetric(root.right, root_copy.left)
        else:
            return False
