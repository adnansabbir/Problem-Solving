from helpers.BST import array_to_bst
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode, extra_data=None) -> int:

        if not extra_data:
            extra_data = {
                'last_visited': None,
                'minimum_val': sys.maxsize
            }

        if root.left:
            self.minDiffInBST(root.left, extra_data)

        if extra_data['last_visited']:
            extra_data['minimum_val'] = min(abs(extra_data['last_visited'].val - root.val), extra_data['minimum_val'])

        extra_data['last_visited'] = root

        if root.right:
            self.minDiffInBST(root.right, extra_data)

        return extra_data['minimum_val']


test_array = [10, 5, 15, 1, 8]
sol = Solution()
print(sol.minDiffInBST(array_to_bst(test_array)))
# print(ord('A'))
