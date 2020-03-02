from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid_of_nums = len(nums) // 2

        root = TreeNode(nums[mid_of_nums])
        root.left = self.sortedArrayToBST(nums[:mid_of_nums])
        root.right = self.sortedArrayToBST(nums[mid_of_nums + 1:])
        return root


sol = Solution()
head = sol.sortedArrayToBST([-10, -3, 0, 5, 9])

# You can check answer using 107 Binary Tree Level Order Traversal
