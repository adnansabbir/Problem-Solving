from helpers.BST import array_to_bst
import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        l_min = r_min = sys.maxsize
        if root.left:
            l_min = min(abs(root.val - root.left.val), self.minDiffInBST(root.left))

        if root.right:
            r_min = min(abs(root.val - root.right.val), self.minDiffInBST(root.right))

        return min(l_min, r_min)


test_array = [4, 2, 6, 10, 20]
sol = Solution()
print(sol.minDiffInBST(array_to_bst(test_array)))
# print(ord('A'))
