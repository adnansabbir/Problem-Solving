class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getKthElementInOrder(self, node: TreeNode, k: int):
        print(node.val, k)

        if not (node.right or node.left):
            return node if k == 1 else k - 1

        if node.left:
            k = self.getKthElementInOrder(node.left, k)
            if not isinstance(k, int):
                return k

        print(node.val, ' has k = ', k)
        if k == 1:
            return node
        else:
            k -= 1

        if node.right:
            k = self.getKthElementInOrder(node.right, k)

        return k

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.getKthElementInOrder(root, k).val
