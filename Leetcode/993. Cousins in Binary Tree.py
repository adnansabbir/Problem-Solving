from helpers.BST import array_to_bst


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.depths = []

    def findCousins(self, node: TreeNode, cousins: [int], depth=0):
        if not node:
            return 0

        if node.val in cousins:
            self.depths.append(depth)
            cousins.remove(node.val)
            return node.val

        if node.right and node.left:
            if node.right.val in cousins and node.left.val in cousins:
                return 0

        self.findCousins(node.left, cousins, depth + 1)
        self.findCousins(node.right, cousins, depth + 1)

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.findCousins(root, [x, y])

        if len(self.depths) == 2 and self.depths[0] == self.depths[1]:
            return True

        return False


sol = Solution()
head = array_to_bst([1, 2, 3, None, 4, None, 5])
print(sol.isCousins(head, 4, 5))
