class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode, is_root=True) -> int:
        if not root:
            return 0

        if is_root:
            self.diameter = 0

        left_length = 0
        right_length = 0

        if root.left:
            left_length = self.diameterOfBinaryTree(root.left, False) + 1

        if root.right:
            right_length = self.diameterOfBinaryTree(root.right, False) + 1

        if left_length + right_length > self.diameter:
            self.diameter = left_length + right_length

        if is_root:
            return self.diameter

        return max(left_length, right_length)


sol = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.left = n2
n1.right = n3
#
n4 = TreeNode(4)
n5 = TreeNode(5)
#
n2.left = n4
n2.right = n5
#
n6 = TreeNode(6)
n7 = TreeNode(7)

n4.left = n6
n6.left = n7
#
n8 = TreeNode(6)
n9 = TreeNode(7)
n5.right = n8
n8.right = n9
#
# n31 = TreeNode(31)
# n32 = TreeNode(31)
# n3.right = n31
# n31.right = n32
print(sol.diameterOfBinaryTree(n1))
